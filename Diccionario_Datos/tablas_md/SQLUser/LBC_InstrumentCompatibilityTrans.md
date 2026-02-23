# SQLUser.LBC_InstrumentCompatibilityTrans

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINCT_ParRef | bigint | PK |  | NO | Parent instrument DR |
| ChildQ33DR | - |  |  | SI | Child Reference: Call notification history |
| LBCINCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINCT_Compatibility | varchar |  |  | SI | Internal Compatibility |
| LBCINCT_DateFrom | date |  |  | SI | Date From |
| LBCINCT_DateTo | date |  |  | SI | Date To |
| LBCINCT_InstrumentCompatibility | varchar |  |  | SI | Instrument Compatibility |
| LBCINCT_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Ward / department |
| Q02 | - |  |  | SI | Parent unit Hospital Medical Officer (HMO)	 |
| Q03 | - |  |  | SI | Date of death	 |
| Q04 | - |  |  | SI | Time of death	 |
| Q05 | - |  |  | SI | Hospital Medical Officer (HMO) declaring death	 |
| Q06 | - |  |  | SI | Death certificate completed	 |
| Q07 | - |  |  | SI | Relatives / next of kin notified |
| Q08 | - |  |  | SI | By whom	 |
| Q09 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Time |
| Q11 | - |  |  | SI | Relatives / next of kin name(s)	 |
| Q12 | - |  |  | SI | General Practitioner (GP) notified |
| Q13 | - |  |  | SI | General Practitioner (GP) name	 |
| Q14 | - |  |  | SI | Date notified	 |
| Q15 | - |  |  | SI | Time notified	 |
| Q16 | - |  |  | SI | Please indicate when notified by Hospital Medical ... |
| Q17 | - |  |  | SI | Please indicate when completed |
| Q18 | - |  |  | SI | Left on deceased (please list)	 |
| Q19 | - |  |  | SI | Sent home with relative / next of kin |
| Q20 | - |  |  | SI | Name(s)	 |
| Q21 | - |  |  | SI | Nurse's name	 |
| Q22 | - |  |  | SI | Witness signature (relative / next of kin)	 |
| Q22UDt | - |  |  | SI | Witness signature (relative / next of kin)	 Last U... |
| Q22UTm | - |  |  | SI | Witness signature (relative / next of kin)	 Last U... |
| Q23 | - |  |  | SI | Witness name (relative / next of kin)	 |
| Q24 | - |  |  | SI | Pacemaker insitu |
| Q25 | - |  |  | SI | Incomplete actions referred to Medical Officer (MO... |
| Q26 | - |  |  | SI | Signature	 |
| Q26UDt | - |  |  | SI | Signature	 Last Updated Date |
| Q26UTm | - |  |  | SI | Signature	 Last Updated Time |
| Q27 | - |  |  | SI | Name |
| Q28 | - |  |  | SI | Date |
| Q29 | - |  |  | SI | Signature	 |
| Q29UDt | - |  |  | SI | Signature	 Last Updated Date |
| Q29UTm | - |  |  | SI | Signature	 Last Updated Time |
| Q30 | - |  |  | SI | Name |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | Valuables sent home |
| Q34 | - |  |  | SI | Reason for not calling |
| Q35 | - |  |  | SI | Room number |
| Q36 | - |  |  | SI | Bed number |
| Q37 | - |  |  | SI | Comments |
| Q38 | - |  |  | SI | Name of Member Representative of Patient (MRP) |
| Q39 | - |  |  | SI | ID ( Member Representative of Patient (MRP)) |
| Q40 | - |  |  | SI | Contact number |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Signature |
| Q42UDt | - |  |  | SI | Signature Last Updated Date |
| Q42UTm | - |  |  | SI | Signature Last Updated Time |
| Q43 | - |  |  | SI | Name of patient experience officer |
| Q44 | - |  |  | SI | ID |
| Q45 | - |  |  | SI | Date |
| Q46 | - |  |  | SI | Signature |
| Q46UDt | - |  |  | SI | Signature Last Updated Date |
| Q46UTm | - |  |  | SI | Signature Last Updated Time |
| Q47 | - |  |  | SI | Dummy 1 |
| Q48 | - |  |  | SI | Dummy 2 |
| Q49 | - |  |  | SI | Dummy 3 |
| Q50 | - |  |  | SI | Dummy 4 |
| Q51 | - |  |  | SI | Dummy 5 |
| Q52 | - |  |  | SI | Dummy 6 |
| Q53 | - |  |  | SI | Dummy 7 |
| Q54 | - |  |  | SI | Dummy 8 |
| Q55 | - |  |  | SI | Dummy 9 |
| Q56 | - |  |  | SI | Dummy 10 |
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