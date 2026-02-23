# SQLUser.LBC_ResultInterpretationRule

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRIR_ParRef | bigint | PK |  | NO | Parent Result Interpretation Rule |
| LBCRIR_Action | varchar |  |  | NO | Action |
| LBCRIR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRIR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCRIR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCRIR_ResultValue | varchar |  |  | SI | Result value |
| LBCRIR_Result_DR | varchar |  | FK | SI | Result  |
| LBCRIR_RowID | varchar |  |  | NO | - |
| LBCRIR_Sequence | double |  |  | NO | Sequence |
| Q01 | - |  |  | SI | Esta basicamente satisfecho con su vida |
| Q02 | - |  |  | SI | Ha renunciado a muchas de sus actividades e intere... |
| Q03 | - |  |  | SI | Siente que su vida esta vacía |
| Q04 | - |  |  | SI | Se encuentra a menudo aburrido |
| Q05 | - |  |  | SI | Tiene esperanza en el futuro |
| Q06 | - |  |  | SI | Sufre molestias por pensamientos que no pueda saca... |
| Q07 | - |  |  | SI | Tiene a menudo buen animo |
| Q08 | - |  |  | SI | Tiene miedo de que algo le este pasando |
| Q09 | - |  |  | SI | Se siente feliz muchas veces |
| Q10 | - |  |  | SI | Se siente a menudo abandonado |
| Q11 | - |  |  | SI | Esta a menudo intranquilo e inquieto |
| Q12 | - |  |  | SI | Prefiere quedarse en casa que acaso salir y hacer ... |
| Q13 | - |  |  | SI | Frecuentemente està preocupado por el futuro |
| Q14 | - |  |  | SI | Encuentra que tiene mas problemas de memoria que l... |
| Q15 | - |  |  | SI | Piensa que es maravilloso vivir |
| Q16 | - |  |  | SI | Se siente a menudo desanimado y melancòlico |
| Q17 | - |  |  | SI | Se siente bastante inùtil en el medio en que està |
| Q18 | - |  |  | SI | Està muy preocupado por el pasado |
| Q19 | - |  |  | SI | Encuentra la vida muy estimulante |
| Q20 | - |  |  | SI | Es difìcil para usted poner en marcha nuevos proye... |
| Q21 | - |  |  | SI | Se siente lleno de energia |
| Q22 | - |  |  | SI | Siente que su situacion es desesperada |
| Q23 | - |  |  | SI | Cree que mucha gente esta mejor que usted |
| Q24 | - |  |  | SI | Frecuentemente esta preocupado por pequeñas cosas |
| Q25 | - |  |  | SI | Frecuentemente siente ganas de llorar |
| Q26 | - |  |  | SI | Tiene problemas para concentrarse |
| Q27 | - |  |  | SI | Se siente mejor por la mañana al levantarse |
| Q28 | - |  |  | SI | Prefiere evitar reuniones sociales |
| Q29 | - |  |  | SI | Es fàcil para usted tomar decisiones |
| Q30 | - |  |  | SI | Su mente esta tan clara como lo acostumbraba a est... |
| Q31 | - |  |  | SI | Puntaje Total Escala |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*