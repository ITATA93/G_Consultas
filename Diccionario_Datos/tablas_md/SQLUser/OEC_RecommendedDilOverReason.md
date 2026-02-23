# SQLUser.OEC_RecommendedDilOverReason

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RDOR_RowId | bigint | PK |  | NO | - |
| ChildQ05DR | - |  |  | SI | Child Reference: Cash |
| Q01 | - |  |  | SI | Objects removed because of therapeutic indication |
| Q01N | - |  |  | SI | Note |
| Q02 | - |  |  | SI | Personal items remaining with the patient |
| Q02N | - |  |  | SI | Note |
| Q03 | - |  |  | SI | Other |
| Q03N | - |  |  | SI | Note |
| Q04 | - |  |  | SI | Clothing |
| Q04N | - |  |  | SI | Note |
| Q05N | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Jewellery |
| Q12 | - |  |  | SI | Items Placed in the Hospital Safe |
| Q13 | - |  |  | SI | Items placed in safe |
| Q14 | - |  |  | SI | Receipt number |
| Q15 | - |  |  | SI | Receipt images |
| Q15TxtOnly | - |  |  | SI | Receipt images Plain Text Only |
| Q16 | - |  |  | SI | General comments |
| Q17 | - |  |  | SI | Patient Aids |
| Q18 | - |  |  | SI | On admission dentures? |
| Q19 | - |  |  | SI | On admission glasses? |
| Q20 | - |  |  | SI | On admission hearing aids? |
| Q21 | - |  |  | SI | Other? Please specify |
| Q22 | - |  |  | SI | On transfer dentures? |
| Q23 | - |  |  | SI | On transfer glasses? |
| Q24 | - |  |  | SI | On transfer hearing aids? |
| Q25 | - |  |  | SI | Is patient able to take responsibility for own per... |
| Q26 | - |  |  | SI | Advise patients / relatives of patients secure loc... |
| Q27 | - |  |  | SI | Where are valuables stored? |
| Q28 | - |  |  | SI | On admission disclaimer patient / relative has had... |
| Q29 | - |  |  | SI | and valuables deposited for safe-keeping, as appro... |
| Q30 | - |  |  | SI | If patient does not have capacity to take responsi... |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | Time |
| Q33 | - |  |  | SI | Items placed in the hospital safe |
| Q34 | - |  |  | SI | I acknowledge that any jewellery or valuables kept... |
| Q35 | - |  |  | SI | Name |
| Q36 | - |  |  | SI | Relationship to patient |
| Q37 | - |  |  | SI | Other relationship |
| Q38 | - |  |  | SI | Date |
| Q39 | - |  |  | SI | Signature |
| Q39UDt | - |  |  | SI | Signature Last Updated Date |
| Q39UTm | - |  |  | SI | Signature Last Updated Time |
| Q40 | - |  |  | SI | Personal Property Disclaimer: |
| Q41 | - |  |  | SI | You are advised to hand to the nurse in charge as ... |
| Q42 | - |  |  | SI | You are responsible for any articles not handed ov... |
| Q43 | - |  |  | SI | in whatever way the loss or damage may occur, unle... |
| Q44 | - |  |  | SI | Wards do not have a safe on them, so therefore pro... |
| Q45 | - |  |  | SI | The cash / jewellery items would need to go to saf... |
| Q46 | - |  |  | SI | A deceased patient property is listed and placed w... |
| Q47 | - |  |  | SI | As for other items there is no other form of secur... |
| Q48 | - |  |  | SI | If this form of property handed other to patients ... |
| Q49 | - |  |  | SI | Patient has acknowledged and understands the above... |
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
| RDOR_Code | varchar |  |  | NO | Code |
| RDOR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RDOR_CreatedDate | date |  |  | SI | Created Date |
| RDOR_CreatedTime | time |  |  | SI | Created Time |
| RDOR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RDOR_DateFrom | date |  |  | SI | Date From |
| RDOR_DateTo | date |  |  | SI | Date To |
| RDOR_Desc | varchar |  |  | NO | Description |
| RDOR_Owner | varchar |  |  | SI | Owner |
| RDOR_UpdatedDate | date |  |  | SI | Updated Date |
| RDOR_UpdatedTime | time |  |  | SI | Updated Time |
| RDOR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*