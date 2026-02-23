# SQLUser.PAC_AllergyList

**Schema:** SQLUser
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALRGLST_RowId | bigint | PK |  | NO | - |
| ALRGLST_Code | varchar |  |  | NO | Code |
| ALRGLST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALRGLST_CreatedDate | date |  |  | SI | Created Date |
| ALRGLST_CreatedTime | time |  |  | SI | Created Time |
| ALRGLST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALRGLST_DateFrom | date |  |  | SI | Date From |
| ALRGLST_DateTo | date |  |  | SI | Date To |
| ALRGLST_Desc | varchar |  |  | NO | Description |
| ALRGLST_ListType | varchar |  |  | SI | Allergen List Type |
| ALRGLST_Owner | varchar |  |  | SI | Owner |
| ALRGLST_UpdatedDate | date |  |  | SI | Updated Date |
| ALRGLST_UpdatedTime | time |  |  | SI | Updated Time |
| ALRGLST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Patient Location at Time of Request |
| Q02 | - |  |  | SI | Ward |
| Q03 | - |  |  | SI | Discharge date |
| Q04 | - |  |  | SI | Delivery details |
| Q05 | - |  |  | SI | Give details |
| Q06 | - |  |  | SI | Select therapy group |
| Q07 | - |  |  | SI | Has the patient been referred to palliative care s... |
| Q08 | - |  |  | SI | Is life expectancy <3 months |
| Q09 | - |  |  | SI | Arterial blood gases taken? |
| Q10 | - |  |  | SI | Diagnostic details |
| Q11 | - |  |  | SI | Provide details |
| Q12 | - |  |  | SI | Right heart failure |
| Q13 | - |  |  | SI | Polycythaemia |
| Q14 | - |  |  | SI | Pulmonary hypertension |
| Q15 | - |  |  | SI | Medication class |
| Q16 | - |  |  | SI | Provide details |
| Q17 | - |  |  | SI | Four week review details |
| Q17TxtOnly | - |  |  | SI | Four week review details Plain Text Only |
| Q18 | - |  |  | SI | Name |
| Q19 | - |  |  | SI | Speciality |
| Q20 | - |  |  | SI | Department |
| Q21 | - |  |  | SI | Phone |
| Q22 | - |  |  | SI | Pager |
| Q23 | - |  |  | SI | Signed |
| Q23UDt | - |  |  | SI | Signed Last Updated Date |
| Q23UTm | - |  |  | SI | Signed Last Updated Time |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | NB. May be signed by either Physician or Chronic R... |
| Q26 | - |  |  | SI | Date |
| Q27 | - |  |  | SI | Room Air |
| Q28 | - |  |  | SI | pH |
| Q29 | - |  |  | SI | PaCO2 (mmHg) |
| Q30 | - |  |  | SI | PaO2 (mmHg) |
| Q31 | - |  |  | SI | SaO2 (%) |
| Q32 | - |  |  | SI | COHb % |
| Q33 | - |  |  | SI | Date |
| Q34 | - |  |  | SI | Awake baseline SpO2 (%) |
| Q35 | - |  |  | SI | Minimum asleep SpO2 (%) |
| Q36 | - |  |  | SI | % Sleep time SpO2 < 88% |
| Q37 | - |  |  | SI | Patient mobility |
| Q38 | - |  |  | SI | Aid detail |
| Q39 | - |  |  | SI | Date |
| Q40 | - |  |  | SI | SpO2 (%) room air |
| Q41 | - |  |  | SI | SpO2 (%) on oxygen |
| Q42 | - |  |  | SI | Select options and specify O2 flow rate and usage |
| Q43 | - |  |  | SI | Oxygen concentrator |
| Q44 | - |  |  | SI | O2 flow (L/min) |
| Q45 | - |  |  | SI | Usage (hrs/day) |
| Q46 | - |  |  | SI | Portable oxygen |
| Q47 | - |  |  | SI | Type |
| Q48 | - |  |  | SI | Cylinder |
| Q49 | - |  |  | SI | O2 flow (L/min) |
| Q50 | - |  |  | SI | Usage (hrs/day) |
| Q51 | - |  |  | SI | Cylinder |
| Q52 | - |  |  | SI | Emergency |
| Q53 | - |  |  | SI | O2 flow (L/min) |
| Q54 | - |  |  | SI | Usage (hrs/day) |
| Q55 | - |  |  | SI | Signature |
| Q55UDt | - |  |  | SI | Signature Last Updated Date |
| Q55UTm | - |  |  | SI | Signature Last Updated Time |
| Q56 | - |  |  | SI | Name |
| Q57 | - |  |  | SI | Destination |
| Q58 | - |  |  | SI | Date |
| Q59 | - |  |  | SI | If Palliative: |
| Q60 | - |  |  | SI | Patient checks |
| Q61 | - |  |  | SI | Delivery address |
| Q62 | - |  |  | SI | Delivery address comments |
| Q63 | - |  |  | SI | Date |
| Q64 | - |  |  | SI | Time |
| Q65 | - |  |  | SI | Provider number |
| Q66 | - |  |  | SI | COHb % |
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