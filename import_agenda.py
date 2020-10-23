#!/usr/bin/python3

from Model.presentation import Presentation
from Model.subsession import Subsession
from Model.session import Session, SessionType
from Model.speaker import Speaker
from db_table import db_table
import sys
import pandas as pd

def import_agenda(filename):
    DATE_COL_IDX = 0
    START_TIME_COL_IDX = 1
    END_TIME_COL_IDX = 2
    SESSION_TYPE_COL_IDX = 3
    SESSION_TITLE_COL_IDX = 4
    LOCATION_COL_IDX = 5
    DESCRIPTION_COL_INDEX = 6
    SPEAKER_COL_INDEX = 7

    df = pd.read_excel(filename,skiprows=[i for i in range(0,14)])
    df = df.fillna('')
    session_table = db_table.create_table("sessions", Session.get_schema());
    speaker_table = db_table.create_table("speaker", Speaker.get_schema());
    subsession_table = db_table.create_table("subsessions", Subsession.get_schema());
    presentation_table = db_table.create_table("presentation", Presentation.get_schema());

    speaker_dict = {}
    parent_session_id = None
    for _index, row in df.iterrows():
        session_id = session_table.insert({
            Session.DATE: row[DATE_COL_IDX],
            Session.START_TIME: row[START_TIME_COL_IDX],
            Session.END_TIME: row[END_TIME_COL_IDX],
            Session.TITLE: row[SESSION_TITLE_COL_IDX],
            Session.LOCATION: row[LOCATION_COL_IDX],
            Session.DESCRIPTION: row[DESCRIPTION_COL_INDEX],
        })

        if row[SESSION_TYPE_COL_IDX] == SessionType.SUBSESSION:
            assert parent_session_id != None
            subsession_id = subsession_table.insert(
                {
                    Subsession.CHILD_SESSION_ID: session_id,
                    Subsession.PARENT_SESSION_ID: parent_session_id
                }
            )
        else: 
            parent_session_id = session_id
        
        if len(row[SPEAKER_COL_INDEX]) > 0:
            speakers = row[SPEAKER_COL_INDEX].split('; ')
            for speaker in speakers:
                speaker_id = speaker_dict.get(speaker, None)
                if not speaker_id:
                    speaker_id = speaker_table.insert(
                        {
                            Speaker.NAME: speaker
                        }
                    )
                presentation_table.insert(
                    {
                        Presentation.SPEAKER_ID: speaker_id,
                        Presentation.SESSION_ID: session_id
                    }
                )


        
