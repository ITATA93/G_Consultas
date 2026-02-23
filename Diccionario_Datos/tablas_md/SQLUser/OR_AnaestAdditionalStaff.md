# SQLUser.OR_AnaestAdditionalStaff

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAAS_ParRef | varchar | PK |  | NO | OR_Anaesthesia Parent Reference |
| ANAAS_CPLocation_DR | bigint |  | FK | SI | Des Resf CT_Loc |
| ANAAS_CareProvType | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017.2+ and re... |
| ANAAS_CareProv_DR | varchar |  | FK | SI | Des Ref CT_CareProv |
| ANAAS_Childsub | double |  |  | NO | Childsub |
| ANAAS_EndDate | date |  |  | SI | End Date |
| ANAAS_EndTime | time |  |  | SI | End Time |
| ANAAS_NonCPAttendeeDetails | varchar |  |  | SI | Non CP Attendee Details |
| ANAAS_OperatingStaffRole_DR | bigint |  | FK | SI | Des Ref ORC_OperatingStaffRole |
| ANAAS_OperatingStaffStatus_DR | bigint |  | FK | SI | Des Ref ORCOperatingStaffStatus |
| ANAAS_Operation_DR | bigint |  | FK | SI | Des Ref ORC_Operation |
| ANAAS_Remarks | varchar |  |  | SI | Remarks |
| ANAAS_RowId | varchar |  |  | NO | - |
| ANAAS_ShiftNumber | varchar |  |  | SI | Shift Number |
| ANAAS_StartDate | date |  |  | SI | Start Date |
| ANAAS_StartTime | time |  |  | SI | Start Time |
| ANAAS_StatePPP_DR | bigint |  | FK | SI | Des Ref PAC_StatePPP |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Fetal Computerised Cardiotocography (cCTG) Assessm... |
| Q04 | - |  |  | SI | Computerised CTG (cCTG) is not indicated in the pr... |
| Q05 | - |  |  | SI | Fetal monitoring equipment checks complete |
| Q06 | - |  |  | SI | Indication for Fetal Monitoring |
| Q07 | - |  |  | SI | Other |
| Q08 | - |  |  | SI | cCTG commenced date and time |
| Q09 | - |  |  | SI | cCTG commenced time |
| Q11 | - |  |  | SI | cCTG discontinued date and time |
| Q12 | - |  |  | SI | cCTG discontinued time |
| Q13 | - |  |  | SI | Consider: |
| Q14 | - |  |  | SI | Has the baby(ies) got good reserve? |
| Q15 | - |  |  | SI | Is the baby(ies) compensating due to intra-uterine... |
| Q16 | - |  |  | SI | Is there evidence of decompensating? |
| Q17 | - |  |  | SI | Clinical Plan & Actions |
| Q18 | - |  |  | SI | Clinical interventions required |
| Q19 | - |  |  | SI | Comments |
| Q20 | - |  |  | SI | DO NOT act on the basis of the cCTG analysis alone... |
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