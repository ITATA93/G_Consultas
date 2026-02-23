# SQLUser.ARC_PayAgreemICD

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICD_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| ICD_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| ICD_Childsub | double |  |  | NO | Childsub |
| ICD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ICD_CreatedDate | date |  |  | SI | Created Date |
| ICD_CreatedTime | time |  |  | SI | Created Time |
| ICD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ICD_ICDDx_DR | bigint |  | FK | SI | Des Ref ICDDx |
| ICD_RowId | varchar |  |  | NO | - |
| ICD_UpdatedDate | date |  |  | SI | Updated Date |
| ICD_UpdatedTime | time |  |  | SI | Updated Time |
| ICD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | Evaluador |
| Q04 | - |  |  | SI | Espero el futuro con esperanza y entusiasmo |
| Q05 | - |  |  | SI | Puedo darme por vencido, renunciar, ya que no pued... |
| Q06 | - |  |  | SI | Cuando las cosas van mal me alivia saber que las n... |
| Q07 | - |  |  | SI | No puedo imaginar como sera mi vida dentro de 10 a... |
| Q08 | - |  |  | SI | Tengo bastante tiempo para llevar a cabo las cosas... |
| Q09 | - |  |  | SI | En el futuro espero poder conseguir los que me pue... |
| Q10 | - |  |  | SI | Mi futuro me parece oscuro |
| Q11 | - |  |  | SI | Espero mas cosas buenas de la vida que lo que la g... |
| Q12 | - |  |  | SI | No logro hacer que las cosas cambien y no existen ... |
| Q13 | - |  |  | SI | Mis pasadas experiencias me han preparado bien par... |
| Q14 | - |  |  | SI | Todo lo que puedo ver hacia adelante es mas desagr... |
| Q15 | - |  |  | SI | No espero conseguir lo que realmente deseo |
| Q16 | - |  |  | SI | Cuando miro hacia el futuro espero que sere mas fe... |
| Q17 | - |  |  | SI | Las cosas no marchan como quisiera |
| Q18 | - |  |  | SI | Tengo una gran confianza en el futuro |
| Q19 | - |  |  | SI | Nunca consigo lo que deseo por lo que es absurdo d... |
| Q20 | - |  |  | SI | Es muy improbable que pueda lograr una satisfaccio... |
| Q21 | - |  |  | SI | El futuro me parece vago e incierto |
| Q22 | - |  |  | SI | Espero mas bien epocas buenas que malas |
| Q23 | - |  |  | SI | No merece la pena que intente conseguir algo que d... |
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