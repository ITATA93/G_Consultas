# questionnaire.QGXXXEDBLDM

> Blood Transfusion Monitoring Chart

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Blood Transfusion Monitoring Chart

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Blood component type |
| Q02 | varchar |  |  | SI | Blood component unit number |
| Q03 | numeric |  |  | SI | Blood component unit volume (mL) |
| Q04 | date |  |  | SI | Expiry date |
| Q05 | varchar |  |  | SI | Weight |
| Q05ObsDR | varchar |  | FK | SI | Weight DR |
| Q06 | date |  |  | SI | Date of transfusion |
| Q07 | time |  |  | SI | Transfusion start time |
| Q08 | time |  |  | SI | Transfusion end time |
| Q09 | varchar |  |  | SI | Blood group |
| Q11 | time |  |  | SI | Total transfusion time |
| Q12 | numeric |  |  | SI | Total amount transfused (ml) |
| Q13 | varchar |  |  | SI | Transfusion status |
| Q14 | varchar |  |  | SI | Complications |
| Q15 | date |  |  | SI | Transfusion end date |
| Q16 | bit |  |  | SI | Patient stated first name, surname and date of bir... |
| Q17 | bit |  |  | SI | ID details match patient's wrist band |
| Q18 | varchar |  |  | SI | Blood group |
| Q18ObsDR | varchar |  | FK | SI | Blood group DR |
| Q20 | varchar |  |  | SI | Signs and symptoms |
| Q21 | bit |  |  | SI | Blood pack correct |
| Q22 | bit |  |  | SI | Blood transfusion record correct |
| Q23 | bit |  |  | SI | Pre transfusion medical checklist completed |
| Q24 | bit |  |  | SI | Pre transfusion nursing checklist completed |
| Q25 | bit |  |  | SI | Post transfusion reaction procedure completed |
| Q27 | varchar |  |  | SI | Total amount transfused (ml)	 |
| Q27ObsDR | varchar |  | FK | SI | Total amount transfused (ml)	 DR |
| Q28 | varchar |  |  | SI | Transfusion start overseen by |
| Q29 | numeric |  |  | SI | Total volume transfused (ml) |
| Q30 | varchar |  |  | SI | Blood group of blood component |
| Q31 | date |  |  | SI | Date |
| Q32 | time |  |  | SI | Time |
| Q33 | varchar |  |  | SI | Suspected adverse transfusion events checklist com... |
| Q34 | varchar |  |  | SI | Pre-transfusion checklist completed |
| Q35 | varchar |  |  | SI | Identification details match patient's wrist band |
| Q36 | varchar |  |  | SI | Blood pack correct |
| Q37 | varchar |  |  | SI | Blood component type |
| Q38 | varchar |  |  | SI | Total transfusion time (min) |
| Q39 | varchar |  |  | SI | Transfusion status |
| Q40 | varchar |  |  | SI | URN |
| Q41 | varchar |  |  | SI | Transfusion started by |
| Q42 | longvarbinary |  |  | SI | Signature |
| Q42UDt | date |  |  | SI | Signature Last Updated Date |
| Q42UTm | time |  |  | SI | Signature Last Updated Time |
| Q43 | longvarbinary |  |  | SI | Signature |
| Q43UDt | date |  |  | SI | Signature Last Updated Date |
| Q43UTm | time |  |  | SI | Signature Last Updated Time |
| Q44 | varchar |  |  | SI | Cell product  cryopreserved? |
| Q45 | varchar |  |  | SI | If cell product cryopreserved where was product th... |
| Q46 | numeric |  |  | SI | Cryo - shipper temperature |
| Q47 | varchar |  |  | SI | Temperature scale |
| Q48 | varchar |  |  | SI | Comments |
| Q49 | varchar |  |  | SI | Values scanned or entered into this URN field are ... |
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