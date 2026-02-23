# questionnaire.QGXXXPP

> Patient Property and Belongings

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Property and Belongings

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Objects removed because of therapeutic indication |
| Q01N | varchar |  |  | SI | Note |
| Q02 | varchar |  |  | SI | Personal items remaining with the patient |
| Q02N | varchar |  |  | SI | Note |
| Q03 | varchar |  |  | SI | Other |
| Q03N | varchar |  |  | SI | Note |
| Q04 | varchar |  |  | SI | Clothing |
| Q04N | varchar |  |  | SI | Note |
| Q05N | varchar |  |  | SI | Note |
| Q11 | varchar |  |  | SI | Jewellery |
| Q12 | bit |  |  | SI | Items Placed in the Hospital Safe |
| Q13 | varchar |  |  | SI | Items placed in safe |
| Q14 | varchar |  |  | SI | Receipt number |
| Q15 | bigint |  |  | SI | Receipt images |
| Q15TxtOnly | bigint |  |  | SI | Receipt images Plain Text Only |
| Q16 | varchar |  |  | SI | General comments |
| Q17 | varchar |  |  | SI | Patient Aids |
| Q18 | varchar |  |  | SI | On admission dentures? |
| Q19 | varchar |  |  | SI | On admission glasses? |
| Q20 | varchar |  |  | SI | On admission hearing aids? |
| Q21 | varchar |  |  | SI | Other? Please specify |
| Q22 | varchar |  |  | SI | On transfer dentures? |
| Q23 | varchar |  |  | SI | On transfer glasses? |
| Q24 | varchar |  |  | SI | On transfer hearing aids? |
| Q25 | varchar |  |  | SI | Is patient able to take responsibility for own per... |
| Q26 | varchar |  |  | SI | Advise patients / relatives of patients secure loc... |
| Q27 | varchar |  |  | SI | Where are valuables stored? |
| Q28 | varchar |  |  | SI | On admission disclaimer patient / relative has had... |
| Q29 | varchar |  |  | SI | and valuables deposited for safe-keeping, as appro... |
| Q30 | varchar |  |  | SI | If patient does not have capacity to take responsi... |
| Q31 | date |  |  | SI | Date |
| Q32 | time |  |  | SI | Time |
| Q33 | varchar |  |  | SI | Items placed in the hospital safe |
| Q34 | varchar |  |  | SI | I acknowledge that any jewellery or valuables kept... |
| Q35 | varchar |  |  | SI | Name |
| Q36 | varchar |  |  | SI | Relationship to patient |
| Q37 | varchar |  |  | SI | Other relationship |
| Q38 | date |  |  | SI | Date |
| Q39 | longvarbinary |  |  | SI | Signature |
| Q39UDt | date |  |  | SI | Signature Last Updated Date |
| Q39UTm | time |  |  | SI | Signature Last Updated Time |
| Q40 | varchar |  |  | SI | Personal Property Disclaimer: |
| Q41 | varchar |  |  | SI | You are advised to hand to the nurse in charge as ... |
| Q42 | varchar |  |  | SI | You are responsible for any articles not handed ov... |
| Q43 | varchar |  |  | SI | in whatever way the loss or damage may occur, unle... |
| Q44 | varchar |  |  | SI | Wards do not have a safe on them, so therefore pro... |
| Q45 | varchar |  |  | SI | The cash / jewellery items would need to go to saf... |
| Q46 | varchar |  |  | SI | A deceased patient property is listed and placed w... |
| Q47 | varchar |  |  | SI | As for other items there is no other form of secur... |
| Q48 | varchar |  |  | SI | If this form of property handed other to patients ... |
| Q49 | varchar |  |  | SI | Patient has acknowledged and understands the above... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*