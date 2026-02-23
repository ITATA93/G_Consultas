# questionnaire.QTCPAINAD

> Escala de Evaluación del Dolor en la Demencia Avanzada (PAINAD)

**Schema:** questionnaire
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Evaluación del Dolor en la Demencia Avanzada (PAINAD)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Assessment Date |
| Q02 | time |  |  | SI | Assessment Time |
| Q03 | varchar |  |  | SI | Comportamiento |
| Q04 | varchar |  |  | SI | Respiración - Independiente de la vocalización |
| Q05 | varchar |  |  | SI | Vocalización negativa |
| Q06 | varchar |  |  | SI | Facial expression |
| Q07 | varchar |  |  | SI | Lenguaje corporal |
| Q08 | varchar |  |  | SI | Capacidad de Alivio |
| Q09 | varchar |  |  | SI | Instructions: |
| Q10 | varchar |  |  | SI | Observe al paciente durante cinco minutos antes de... |
| Q11 | varchar |  |  | SI | activity, during caregiving, after the administrat... |
| Q12 | varchar |  |  | SI | The total score ranges from 0-10 points. |
| Q13 | varchar |  |  | SI | Breathing |
| Q14 | varchar |  |  | SI | 	 1. Normal breathing is characterized by effortle... |
| Q15 | varchar |  |  | SI |  2. Occasional labored breathing is characterized ... |
| Q16 | varchar |  |  | SI |  3. Short period of hyperventilation is characteri... |
| Q17 | varchar |  |  | SI |  4. Noisy labored breathing is characterized by ne... |
| Q18 | varchar |  |  | SI | 	 5. Long period of hyperventilation is characteri... |
| Q19 | varchar |  |  | SI |  6. Cheyne-Stokes respirations are characterized b... |
| Q20 | varchar |  |  | SI | Negative Vocalization |
| Q21 | varchar |  |  | SI |  1. None is characterized by speech or vocalizatio... |
| Q22 | varchar |  |  | SI | 	 2. Occasional moan or groan is characterized by ... |
| Q23 | varchar |  |  | SI |  3. Low level speech with a negative or disapprovi... |
| Q24 | varchar |  |  | SI | 	 4. Repeated troubled calling out is characterize... |
| Q25 | varchar |  |  | SI |  5. Loud moaning or groaning is characterized by m... |
| Q26 | varchar |  |  | SI | abruptly beginning and ending. |
| Q27 | varchar |  |  | SI |  6. Crying is characterized by an utterance of emo... |
| Q28 | varchar |  |  | SI |  Facial Expression |
| Q29 | varchar |  |  | SI |  1. Smiling or inexpressive. Smiling is characteri... |
| Q30 | varchar |  |  | SI |  2. Sad is characterized by an unhappy, lonesome, ... |
| Q31 | varchar |  |  | SI |  3. Frightened is characterized by a look of fear,... |
| Q32 | varchar |  |  | SI |  4. Frown is characterized by a downward turn of t... |
| Q33 | varchar |  |  | SI |  5. Facial grimacing is characterized by a distort... |
| Q34 | varchar |  |  | SI | Body Language |
| Q35 | varchar |  |  | SI |  1. Relaxed is characterized by a calm, restful, m... |
| Q36 | varchar |  |  | SI |  2. Tense is characterized by a strained, apprehen... |
| Q37 | varchar |  |  | SI |  3. Distressed pacing is characterized by activity... |
| Q38 | varchar |  |  | SI |  4. Fidgeting is characterized by restless movemen... |
| Q39 | varchar |  |  | SI | be observed. |
| Q40 | varchar |  |  | SI |  5. Rigid is characterized by stiffening of the bo... |
| Q41 | varchar |  |  | SI |  6. Fists clenched is characterized by tightly clo... |
| Q42 | varchar |  |  | SI |  7. Knees pulled up is characterized by flexing th... |
| Q43 | varchar |  |  | SI | 8. Pulling or pushing away is characterized by res... |
| Q44 | varchar |  |  | SI |  9. Striking out is characterized by hitting, kick... |
| Q45 | varchar |  |  | SI | Consolability |
| Q46 | varchar |  |  | SI |  1. No need to console is characterized by a sense... |
| Q47 | varchar |  |  | SI | 	 2. Distracted or reassured by voice or touch is ... |
| Q48 | varchar |  |  | SI | person is at all distressed. |
| Q49 | varchar |  |  | SI | 3. Unable to console, distract, or reassure is cha... |
| Q50 | varchar |  |  | SI | Clasificación de Puntaje |
| Q51 | varchar |  |  | SI |  0: Sin dolor |
| Q52 | varchar |  |  | SI | 1 - 3: Dolor Leve |
| Q53 | varchar |  |  | SI | 4 - 6: Dolor Moderado |
| Q54 | varchar |  |  | SI | 7 - 10: Dolor Severo |
| Q55 | varchar |  |  | SI | The Pain Assessment in Advanced Dementia Scale (PA... |
| Q56 | varchar |  |  | SI | using standard pain scales. |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*