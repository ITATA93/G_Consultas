# SQLUser.CT_LocPharmReview

**Schema:** SQLUser
**Columnas:** 164
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHREV_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| PHREV_Childsub | double |  |  | NO | Childsub |
| PHREV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHREV_CreatedDate | date |  |  | SI | Created Date |
| PHREV_CreatedTime | time |  |  | SI | Created Time |
| PHREV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHREV_DateFrom | date |  |  | SI | DateFrom |
| PHREV_DateTo | date |  |  | SI | DateTo |
| PHREV_EnabledRev | varchar |  |  | SI | Enabled Review |
| PHREV_InclDisOrders | varchar |  |  | SI | Include Discontinued Orders  |
| PHREV_MandatoryBeforeAdmin | varchar |  |  | SI | Mandatory Before Administration  |
| PHREV_MandatoryBeforePack | varchar |  |  | SI | Mandatory Before Pack |
| PHREV_RowId | varchar |  |  | NO | - |
| PHREV_UpdPharmStatus | varchar |  |  | SI | Update Pharmacy Status |
| PHREV_UpdatedDate | date |  |  | SI | Updated Date |
| PHREV_UpdatedTime | time |  |  | SI | Updated Time |
| PHREV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Please enter details of any notable family history... |
| Q02 | - |  |  | SI | Diabetes |
| Q02A | - |  |  | SI | Type 1 diabetes |
| Q02A1 | - |  |  | SI | Relative |
| Q02AT | - |  |  | SI | Details |
| Q02B | - |  |  | SI | Type 2 diabetes |
| Q02B1 | - |  |  | SI | Relative |
| Q02BT | - |  |  | SI | Details |
| Q02C | - |  |  | SI | Type unknown |
| Q02C1 | - |  |  | SI | Relative |
| Q02CT | - |  |  | SI | Details |
| Q03 | - |  |  | SI | Haemoglobinopathy |
| Q03A | - |  |  | SI | Relative |
| Q03T | - |  |  | SI | Details |
| Q04 | - |  |  | SI | Hypertensive disorder |
| Q04A | - |  |  | SI | Relative |
| Q04T | - |  |  | SI | Details |
| Q05 | - |  |  | SI | Pregnancy induced hypertension |
| Q05A | - |  |  | SI | Relative |
| Q05T | - |  |  | SI | Details |
| Q06 | - |  |  | SI | Pre-eclampsia |
| Q06A | - |  |  | SI | Relative |
| Q06T | - |  |  | SI | Details |
| Q07 | - |  |  | SI | Eclampsia |
| Q07A | - |  |  | SI | Relative |
| Q07T | - |  |  | SI | Details |
| Q08 | - |  |  | SI | Congenital hypothyroidism |
| Q08A | - |  |  | SI | Relative |
| Q08T | - |  |  | SI | Details |
| Q09 | - |  |  | SI | Thrombosis |
| Q09A | - |  |  | SI | Relative |
| Q09T | - |  |  | SI | Details |
| Q10 | - |  |  | SI | Tuberculosis |
| Q106 | - |  |  | SI | Date |
| Q107 | - |  |  | SI | Time |
| Q10A | - |  |  | SI | Relative |
| Q10T | - |  |  | SI | Details |
| Q11 | - |  |  | SI | Hearing loss from childhood |
| Q11A | - |  |  | SI | Relative |
| Q11T | - |  |  | SI | Details |
| Q12 | - |  |  | SI | Learning disabilities |
| Q12A | - |  |  | SI | Relative |
| Q12T | - |  |  | SI | Details |
| Q13 | - |  |  | SI | Mental health problems |
| Q13A | - |  |  | SI | Bipolar disorder |
| Q13A1 | - |  |  | SI | Relative |
| Q13AT | - |  |  | SI | Details |
| Q13B | - |  |  | SI | Depression |
| Q13B1 | - |  |  | SI | Relative |
| Q13BT | - |  |  | SI | Details |
| Q13C | - |  |  | SI | Obsessive compulsive disorder |
| Q13C1 | - |  |  | SI | Relative |
| Q13CT | - |  |  | SI | Details |
| Q13D | - |  |  | SI | Schizophrenia |
| Q13D1 | - |  |  | SI | Relative |
| Q13DT | - |  |  | SI | Details |
| Q13E | - |  |  | SI | Other mental health problems |
| Q13E1 | - |  |  | SI | Relative |
| Q13ET | - |  |  | SI | Details |
| Q14 | - |  |  | SI | Congenital anomaly |
| Q14A | - |  |  | SI | Relative |
| Q14T | - |  |  | SI | Details |
| Q15 | - |  |  | SI | MCADD |
| Q15A | - |  |  | SI | Relative |
| Q15T | - |  |  | SI | Details |
| Q16 | - |  |  | SI | Congenital dislocation of hip |
| Q16A | - |  |  | SI | Relative |
| Q16T | - |  |  | SI | Details |
| Q17 | - |  |  | SI | Multiple pregnancy (not IVF etc) |
| Q17A | - |  |  | SI | Relative |
| Q17T | - |  |  | SI | Details |
| Q18 | - |  |  | SI | Cardiac problems from birth |
| Q18A | - |  |  | SI | Relative |
| Q18T | - |  |  | SI | Details |
| Q19 | - |  |  | SI | Childhood eye disorder |
| Q19A | - |  |  | SI | Relative |
| Q19T | - |  |  | SI | Details |
| Q20 | - |  |  | SI | Clotting disorder |
| Q20A | - |  |  | SI | Relative |
| Q20T | - |  |  | SI | Details |
| Q21 | - |  |  | SI | Congenital adrenal hypoplasia |
| Q21A | - |  |  | SI | Relative |
| Q21T | - |  |  | SI | Details |
| Q22 | - |  |  | SI | Cystic fibrosis |
| Q22A | - |  |  | SI | Relative |
| Q22T | - |  |  | SI | Details |
| Q23 | - |  |  | SI | Genetic problems |
| Q23A | - |  |  | SI | Relative |
| Q23T | - |  |  | SI | Details |
| Q24 | - |  |  | SI | PKU |
| Q24A | - |  |  | SI | Relative |
| Q24T | - |  |  | SI | Details |
| Q25 | - |  |  | SI | Other metabolic disorders (not MCADD or PKU) |
| Q25A | - |  |  | SI | Relative |
| Q25T | - |  |  | SI | Details |
| Q26 | - |  |  | SI | Venous thromboembolism |
| Q26A | - |  |  | SI | Relative |
| Q26T | - |  |  | SI | Details |
| Q27 | - |  |  | SI | Other major disease or condition |
| Q27A | - |  |  | SI | Relative |
| Q27T | - |  |  | SI | Details |
| Q28 | - |  |  | SI | Sudden infant death syndrome |
| Q28A | - |  |  | SI | Relative |
| Q28T | - |  |  | SI | Details |
| Q29 | - |  |  | SI | Stillbirths or multiple miscarriages |
| Q29A | - |  |  | SI | Relative |
| Q29T | - |  |  | SI | Details |
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