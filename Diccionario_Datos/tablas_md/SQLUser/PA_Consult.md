# SQLUser.PA_Consult

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONS_RowId | bigint | PK |  | NO | - |
| CONS_Person_DR | bigint |  | FK | SI | Des Ref Person |
| Q01 | - |  |  | SI | Date of examination |
| Q02 | - |  |  | SI | Time of examination |
| Q03 | - |  |  | SI | These are statements that many people have used to... |
| Q04 | - |  |  | SI | My voice makes it difficult for people to hear me |
| Q05 | - |  |  | SI | People have difficulty understanding me in a noisy... |
| Q06 | - |  |  | SI | My family has difficulty hearing me when I call th... |
| Q07 | - |  |  | SI | I use the phone less often than I would like to |
| Q08 | - |  |  | SI | I tend to avoid groups of people because of my voi... |
| Q09 | - |  |  | SI | I speak with friends, neighbours, or relatives les... |
| Q10 | - |  |  | SI | People ask me to repeat myself when speaking face-... |
| Q11 | - |  |  | SI | My voice difficulties restrict my personal and soc... |
| Q12 | - |  |  | SI | I feel left out of conversations because of my voi... |
| Q13 | - |  |  | SI | My voice problem causes me to lose income |
| Q14 | - |  |  | SI | I run out of air when I talk |
| Q15 | - |  |  | SI | The sound of my voice varies throughout the day |
| Q16 | - |  |  | SI | People ask, What's wrong with your voice? |
| Q17 | - |  |  | SI | My voice sounds creaky and dry |
| Q18 | - |  |  | SI | I feel as though I have to strain to produce voice |
| Q19 | - |  |  | SI | The clarity of my voice is unpredictable |
| Q20 | - |  |  | SI | I try to change my voice to sound different |
| Q21 | - |  |  | SI | I use a great deal of effort to speak |
| Q22 | - |  |  | SI | My voice is worse in the evening |
| Q23 | - |  |  | SI | My voice gives out on me in the middle of speaking |
| Q24 | - |  |  | SI | I am tense when talking to others because of my vo... |
| Q25 | - |  |  | SI | People seem irritated with my voice |
| Q26 | - |  |  | SI | I find other people do not understand my voice pro... |
| Q27 | - |  |  | SI | My voice problem upsets me |
| Q28 | - |  |  | SI | I am less outgoing because of my voice problem |
| Q29 | - |  |  | SI | My voice makes me feel handicapped |
| Q30 | - |  |  | SI | I feel annoyed when people ask me to repeat |
| Q31 | - |  |  | SI | I feel embarrassed when people ask me to repeat |
| Q32 | - |  |  | SI | My voice makes me feel incompetent |
| Q33 | - |  |  | SI | I am ashamed of my voice problem |
| Q34 | - |  |  | SI | These are statements that many people have used to... |
| Q35 | - |  |  | SI | Score |
| Q36 | - |  |  | SI | : |
| Q37 | - |  |  | SI | Classification |
| Q38 | - |  |  | SI | 0 - 30 : Mild - Minimal amount of handicap |
| Q39 | - |  |  | SI | 31 - 60 : Moderate - Often seen in patients with v... |
| Q40 | - |  |  | SI | 60 - 120 : Severe - Often seen in patients with vo... |
| Q41 | - |  |  | SI | The Voice Handicap Index is a tool for assessment ... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*