# SQLUser.LB_TestSetImageFile

**Schema:** SQLUser
**Columnas:** 58
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTSIF_ParRef | bigint | PK |  | NO | Parent TestSet DR |
| LBTSIF_AttachToEPR | bit |  |  | SI | Attach to EPR |
| LBTSIF_Comments | varchar |  |  | SI | File comments |
| LBTSIF_Desc | varchar |  |  | SI | File description |
| LBTSIF_FileType | varchar |  |  | SI | Type of the image file JPG, BMP, SVG, etc... |
| LBTSIF_Image_DR | bigint |  | FK | SI | websys.document that stores the image data |
| LBTSIF_RawData | longvarchar |  |  | SI | If the image is a SVG this property stores the raw... |
| LBTSIF_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | ¿Has pensado alguna vez que la vida no vale la pen... |
| Q02 | - |  |  | SI | ¿Has deseado alguna vez estar muerto? |
| Q03 | - |  |  | SI | ¿Has pensado alguna vez terminar con tu vida? |
| Q04 | - |  |  | SI | ¿Has Intentado Suicidarte? |
| Q05 | - |  |  | SI | Resultado Escala de Okasha |
| Q05ObsDR | - |  |  | SI | Resultado Escala de Okasha DR |
| Q06 | - |  |  | SI | Subpuntaje de Ideación Suicida |
| Q07 | - |  |  | SI | Escala auto administrada |
| Q08 | - |  |  | SI | Formada por 4 preguntas, donde las tres primeras e... |
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