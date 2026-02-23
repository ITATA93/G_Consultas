# SQLUser.CT_Loc_MRType

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRTYPE_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| MRTYPE_AdmType | varchar |  |  | SI | Admission Type |
| MRTYPE_Childsub | double |  |  | NO | Childsub |
| MRTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MRTYPE_CreatLocation_DR | bigint |  | FK | SI | Des Ref CTLOC |
| MRTYPE_CreateIfNew | varchar |  |  | SI | Create If New |
| MRTYPE_CreatedDate | date |  |  | SI | Created Date |
| MRTYPE_CreatedTime | time |  |  | SI | Created Time |
| MRTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MRTYPE_Link | double |  |  | SI | Link |
| MRTYPE_MRVolume_DR | varchar |  | FK | SI | Des Ref MR Volume |
| MRTYPE_Prompt | varchar |  |  | SI | Prompt |
| MRTYPE_RowId | varchar |  |  | NO | - |
| MRTYPE_Type_DR | bigint |  | FK | SI | Des Ref MR Type |
| MRTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| MRTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| MRTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| MRTYPE_VolumeDesc | varchar |  |  | SI | Volume Description |
| Q1 | - |  |  | SI | Contraindications for the use of Nitrous Oxide gas |
| Q10 | - |  |  | SI | Use during Myringoplasty. |
| Q11 | - |  |  | SI | Any recent eye procedure that has required injecti... |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | Time |
| Q2 | - |  |  | SI | If the answer to any of the below is 'Yes', the pa... |
| Q3 | - |  |  | SI | Previous or current air embolism. |
| Q4 | - |  |  | SI | Artificial, traumatic or spontaneous pneumothorax. |
| Q5 | - |  |  | SI | Decompression sickness (the bends) or if you have ... |
| Q6 | - |  |  | SI | Severe bullous emphysema. |
| Q7 | - |  |  | SI | Following air encephalography. |
| Q8 | - |  |  | SI | Gross abdominal distension or where there is trapp... |
| Q9 | - |  |  | SI | Raised intracranial pressure or head injury. |
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