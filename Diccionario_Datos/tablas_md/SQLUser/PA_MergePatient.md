# SQLUser.PA_MergePatient

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRG_RowId | bigint | PK |  | NO | - |
| MRG_Date | date |  |  | SI | Date |
| MRG_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| MRG_PAPMI_From_DR | bigint |  | FK | SI | Des Ref PAPMIFrom |
| MRG_PAPMI_To_DR | bigint |  | FK | SI | Des Ref PAPMI |
| MRG_ReasonForMerging_DR | bigint |  | FK | SI | Des Ref ReasonForMerging |
| MRG_ReasonForOverride_DR | bigint |  | FK | SI | Reason for Override  |
| MRG_Time | time |  |  | SI | Time |
| MRG_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Resultado |
| Q01ObsDR | - |  |  | SI | Resultado DR |
| Q02 | - |  |  | SI | I. Anamnesis |
| Q03 | - |  |  | SI | ¿El niño(a) presenta una condición que disminuya s... |
| Q04 | - |  |  | SI | ¿El niño(a) presenta situación de discapacidad? Co... |
| Q05 | - |  |  | SI | II. Condición Clínica |
| Q06 | - |  |  | SI | ¿El niño(a) presenta manchas blancas o COPD&gt |
| Q07 | - |  |  | SI | ¿Cuál es el estado de las encias del niño(a)? |
| Q08 | - |  |  | SI | IV. Dieta |
| Q09 | - |  |  | SI | ¿Cuántas veces al día el niño(a) ingiere alimentos... |
| Q10 | - |  |  | SI | ¿En qué momento el niño(a) realiza la ingesta de a... |
| Q11 | - |  |  | SI | ¿El niño(a) ingiere líquidos y/o alimentos azucara... |
| Q12 | - |  |  | SI | III. Higiene |
| Q13 | - |  |  | SI | ¿Cuántas veces al día se lava los dientes el niño(... |
| Q14 | - |  |  | SI | ¿El niño o niña, se lava los dientes antes de ir a... |
| Q15 | - |  |  | SI | Los padres y/o cuidadores, ¿Supervisan el lavado d... |
| Q16 | - |  |  | SI | V. Fluoruros |
| Q17 | - |  |  | SI | Luego de las preguntas anteriores, según usted (de... |
| Q18 | - |  |  | SI | VI. Motivación de los Padres / Cuidadores |
| Q19 | - |  |  | SI | ¿Utiliza el niño o niña pasta de dientes con 1000-... |
| Q20 | - |  |  | SI | VII. Otros: Habitos y Mal Oclusiones |
| Q21 | - |  |  | SI | ¿El niño(a) se succiona el dedo de modo persistent... |
| Q22 | - |  |  | SI | ¿El niño(a) ocupa chupete entretención, mamadera u... |
| Q23 | - |  |  | SI | ¿El niño(a) presenta mal oclusiones? |
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