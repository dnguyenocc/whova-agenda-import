#!/usr/bin/python3
from Model.presentation import Presentation
import sys


from Model.subsession import Subsession
from Model.session import Session, SessionType
from Model.speaker import Speaker
from db_table import db_table

session_table = db_table("sessions", Session.get_schema());
speaker_table = db_table("speaker", Speaker.get_schema());
subsession_table = db_table("subsessions", Subsession.get_schema());
presentation_table = db_table("presentation", Presentation.get_schema());

def lookup_agenda(column, value):
    sessions = []
    if column in {Session.DATE, 
                    Session.START_TIME, 
                    Session.END_TIME, 
                    Session.TITLE, 
                    Session.LOCATION, 
                    Session.DESCRIPTION }:
        sessions.extend(session_table.select([],{column: value}))
    elif column == 'speaker':
        speakers = speaker_table.select([], {Speaker.NAME: value})
        for speaker in speakers:
            presentations = presentation_table.select([], {Presentation.SPEAKER_ID: speaker[Speaker.ID]})
            for presentation in presentations:
                sessions.extend(session_table.select([], {Session.ID: presentation[Presentation.SESSION_ID]}))

    add_subsession(sessions)
    add_speakers(sessions)
    print(sessions)

def add_subsession(sessions):
    existing_subsession_ids = set()
    subsession_ids = set()
    for session in sessions:
        if session[Session.TYPE] == SessionType.Session.value:
            subsessions = subsession_table.select([Subsession.CHILD_SESSION_ID], {Subsession.PARENT_SESSION_ID: session[Session.ID]})
            for sub in subsessions:
                subsession_ids.add(sub[Subsession.CHILD_SESSION_ID])
        else:
            existing_subsession_ids.add(session[Session.ID])
    for id in existing_subsession_ids:
        subsession_ids.discard(id)

    for id in list(subsession_ids):
        sessions.extend(session_table.select([], {Session.ID: id}))


def add_speakers(sessions):
    for i in range(len(sessions)):
        speaker_ids = presentation_table.select([Presentation.SPEAKER_ID], {Presentation.SESSION_ID: sessions[i][Session.ID]})
        sessions[i][Session.SPEAKER] = []
        for sid in speaker_ids:
            name = speaker_table.select([Speaker.NAME], {Speaker.ID: sid[Presentation.SPEAKER_ID]})
            sessions[i][Session.SPEAKER].append(name[0][Speaker.NAME])

lookup_agenda(sys.argv[1], sys.argv[2])