# SQLUser.CT_TaskDisposition

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTASKDISP_RowId | bigint | PK |  | NO | - |
| CTTASKDISP_Code | varchar |  |  | NO | Sex Code |
| CTTASKDISP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTTASKDISP_DateFrom | date |  |  | SI | Date From |
| CTTASKDISP_DateTo | date |  |  | SI | Date To |
| CTTASKDISP_Desc | varchar |  |  | NO | Sex Description |
| CTTASKDISP_Owner | varchar |  |  | SI | Owner |
| Q01 | - |  |  | SI | Blood component type |
| Q02 | - |  |  | SI | Blood component unit number |
| Q03 | - |  |  | SI | Blood component unit volume (mL) |
| Q04 | - |  |  | SI | Expiry date |
| Q05 | - |  |  | SI | Weight |
| Q05ObsDR | - |  |  | SI | Weight DR |
| Q06 | - |  |  | SI | Date of transfusion |
| Q07 | - |  |  | SI | Transfusion start time |
| Q08 | - |  |  | SI | Transfusion end time |
| Q09 | - |  |  | SI | Blood group |
| Q11 | - |  |  | SI | Total transfusion time |
| Q12 | - |  |  | SI | Total amount transfused (ml) |
| Q13 | - |  |  | SI | Transfusion status |
| Q14 | - |  |  | SI | Complications |
| Q15 | - |  |  | SI | Transfusion end date |
| Q16 | - |  |  | SI | Patient stated first name, surname and date of bir... |
| Q17 | - |  |  | SI | ID details match patient's wrist band |
| Q18 | - |  |  | SI | Blood group |
| Q18ObsDR | - |  |  | SI | Blood group DR |
| Q20 | - |  |  | SI | Signs and symptoms |
| Q21 | - |  |  | SI | Blood pack correct |
| Q22 | - |  |  | SI | Blood transfusion record correct |
| Q23 | - |  |  | SI | Pre transfusion medical checklist completed |
| Q24 | - |  |  | SI | Pre transfusion nursing checklist completed |
| Q25 | - |  |  | SI | Post transfusion reaction procedure completed |
| Q27 | - |  |  | SI | Total amount transfused (ml)	 |
| Q27ObsDR | - |  |  | SI | Total amount transfused (ml)	 DR |
| Q28 | - |  |  | SI | Transfusion start overseen by |
| Q29 | - |  |  | SI | Total volume transfused (ml) |
| Q30 | - |  |  | SI | Blood group of blood component |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | Time |
| Q33 | - |  |  | SI | Suspected adverse transfusion events checklist com... |
| Q34 | - |  |  | SI | Pre-transfusion checklist completed |
| Q35 | - |  |  | SI | Identification details match patient's wrist band |
| Q36 | - |  |  | SI | Blood pack correct |
| Q37 | - |  |  | SI | Blood component type |
| Q38 | - |  |  | SI | Total transfusion time (min) |
| Q39 | - |  |  | SI | Transfusion status |
| Q40 | - |  |  | SI | URN |
| Q41 | - |  |  | SI | Transfusion started by |
| Q42 | - |  |  | SI | Signature |
| Q42UDt | - |  |  | SI | Signature Last Updated Date |
| Q42UTm | - |  |  | SI | Signature Last Updated Time |
| Q43 | - |  |  | SI | Signature |
| Q43UDt | - |  |  | SI | Signature Last Updated Date |
| Q43UTm | - |  |  | SI | Signature Last Updated Time |
| Q44 | - |  |  | SI | Cell product  cryopreserved? |
| Q45 | - |  |  | SI | If cell product cryopreserved where was product th... |
| Q46 | - |  |  | SI | Cryo - shipper temperature |
| Q47 | - |  |  | SI | Temperature scale |
| Q48 | - |  |  | SI | Comments |
| Q49 | - |  |  | SI | Values scanned or entered into this URN field are ... |
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