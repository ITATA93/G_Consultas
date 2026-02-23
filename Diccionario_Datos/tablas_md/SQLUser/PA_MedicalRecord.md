# SQLUser.PA_MedicalRecord

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRN_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| MRN_Childsub | double |  |  | NO | Childsub |
| MRN_No | varchar |  |  | SI | MRN No |
| MRN_RefHosp_DR | bigint |  | FK | SI | Des Ref RefHosp |
| MRN_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Resultado |
| Q01ObsDR | - |  |  | SI | Resultado DR |
| Q02 | - |  |  | SI | I. Anamnesis |
| Q03 | - |  |  | SI | ¿El/la adolescente presenta una condición que dism... |
| Q04 | - |  |  | SI | ¿El/la adolescente presenta situación de discapaci... |
| Q05 | - |  |  | SI | II. Condición Clínica |
| Q06 | - |  |  | SI | ¿El/la adolescente presenta manchas blancas o COPD... |
| Q07 | - |  |  | SI | ¿Cuál es el estado de las encías del/la adolescent... |
| Q08 | - |  |  | SI | IV. Dieta |
| Q09 | - |  |  | SI | ¿Cuántas veces al día el/la adolescente ingiere al... |
| Q10 | - |  |  | SI | ¿En qué momento el/la adolescente realiza la inges... |
| Q11 | - |  |  | SI | ¿El/la adolescente ingiere líquidos y/o alimentos ... |
| Q12 | - |  |  | SI | III. Higiene |
| Q13 | - |  |  | SI | ¿Cuántas veces al día se cepilla los dientes el/la... |
| Q14 | - |  |  | SI | ¿El/la adolescente se lava los dientes antes de ir... |
| Q16 | - |  |  | SI | V. Fluoruros |
| Q17 | - |  |  | SI | Luego de las preguntas anteriores, según usted (de... |
| Q18 | - |  |  | SI | VI. Motivación de los Padres / Cuidadores |
| Q19 | - |  |  | SI | ¿Utiliza el/la adolescente pasta de dientes con 10... |
| Q20 | - |  |  | SI | VII. Otros: Habitos y Mal Oclusiones |
| Q21 | - |  |  | SI | ¿El/la adolescente presenta malos hábitos como oni... |
| Q22 | - |  |  | SI | ¿El/la adolescente presenta mal oclusiones? |
| Q23 | - |  |  | SI | ¿El/la adolescente manifiesta consumo de tabaco, a... |
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