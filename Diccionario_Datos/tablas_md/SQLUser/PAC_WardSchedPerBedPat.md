# SQLUser.PAC_WardSchedPerBedPat

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WBP_ParRef | bigint | PK |  | NO | PAC_WardSchedPer Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | The patient / guardian acknowledges that: |
| Q04 | - |  |  | SI | 1. The hospital has a smoke free policy in place |
| Q05 | - |  |  | SI | 2. Smoking is banned on hospital property includin... |
| Q06 | - |  |  | SI | 3. Nicotine Replacement Therapy (NRT) is available |
| Q07 | - |  |  | SI | 4. Smoking while receiving care is bad for my heal... |
| Q08 | - |  |  | SI | 5. Should I leave hospital property to smoke, I ag... |
| Q09 | - |  |  | SI | 6. I need to inform staff caring for me should I g... |
| Q10 | - |  |  | SI | 7. This Agreement remains valid for the duration o... |
| Q11 | - |  |  | SI | Patient declined to sign form |
| Q12 | - |  |  | SI | Patient unable to sign form |
| Q13 | - |  |  | SI | Person responsible for signing agreement |
| Q14 | - |  |  | SI | Patient signature |
| Q14UDt | - |  |  | SI | Patient signature Last Updated Date |
| Q14UTm | - |  |  | SI | Patient signature Last Updated Time |
| Q15 | - |  |  | SI | Guardian signature |
| Q15UDt | - |  |  | SI | Guardian signature Last Updated Date |
| Q15UTm | - |  |  | SI | Guardian signature Last Updated Time |
| Q16 | - |  |  | SI | Signature of witness |
| Q16UDt | - |  |  | SI | Signature of witness Last Updated Date |
| Q16UTm | - |  |  | SI | Signature of witness Last Updated Time |
| Q17 | - |  |  | SI | Witness name |
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
| WBP_AdmDayOfWeek | varchar |  |  | SI | AdmDayOfWeek |
| WBP_Bed_DR | varchar |  | FK | SI | Des Ref PACBed                  |
| WBP_Childsub | double |  |  | NO | Childsub |
| WBP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WBP_CreatedDate | date |  |  | SI | Created Date |
| WBP_CreatedTime | time |  |  | SI | Created Time |
| WBP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WBP_ExpectedLength | double |  |  | SI | ExpectedLength                  |
| WBP_FreeText1 | varchar |  |  | SI | FreeText1  |
| WBP_FreeText2 | varchar |  |  | SI | FreeText2 |
| WBP_FreeText3 | varchar |  |  | SI | FreeText3 |
| WBP_MinDaysNumBook | double |  |  | SI | MinimumDaysNumberBooking                  |
| WBP_NoAnaesthesia | varchar |  |  | SI | NoAnaesthesia |
| WBP_OperationGroup | varchar |  |  | SI | OperationGroup |
| WBP_OperationOffset | double |  |  | SI | OperationOffset                  |
| WBP_RowId | varchar |  |  | NO | - |
| WBP_UpdatedDate | date |  |  | SI | Updated Date |
| WBP_UpdatedTime | time |  |  | SI | Updated Time |
| WBP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WBP_WeekNumber | double |  |  | SI | WeekNumber                  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*