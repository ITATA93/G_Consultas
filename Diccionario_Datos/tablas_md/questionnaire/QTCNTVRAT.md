# questionnaire.QTCNTVRAT

> Neonatal Tissue Viability Risk Assessment Tool

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neonatal Tissue Viability Risk Assessment Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Intensity and duration of pressure |
| Q04 | varchar |  |  | SI | General physical condition |
| Q05 | varchar |  |  | SI | Mobility |
| Q06 | varchar |  |  | SI | Activity |
| Q07 | varchar |  |  | SI | Sensory perception |
| Q08 | varchar |  |  | SI | Tolerance of the skin and supporting structure |
| Q09 | varchar |  |  | SI | Moisture |
| Q10 | varchar |  |  | SI | Friction |
| Q11 | varchar |  |  | SI | Nutrition |
| Q12 | varchar |  |  | SI | Tissue perfusion and oxygenation |
| Q13 | varchar |  |  | SI | Definitions |
| Q14 | varchar |  |  | SI | Mobility: The ability to change and control body p... |
| Q15 | varchar |  |  | SI | Activity: The degree of physical activity.	 |
| Q16 | varchar |  |  | SI | Sensory perception: The ability to respond in a de... |
| Q17 | varchar |  |  | SI | Moisture: Degree to which skin is exposed to moist... |
| Q18 | varchar |  |  | SI | Friction: (ie babies on CPAP).	 |
| Q19 | varchar |  |  | SI | Nutrition: Usual milk / fluid intake pattern. |
| Q20 | varchar |  |  | SI | 20 or over: Very high risk |
| Q21 | varchar |  |  | SI | Refer to tissue viability link nurses / specialist... |
| Q22 | varchar |  |  | SI | Implement regular position regular position change... |
| Q23 | varchar |  |  | SI | Use gel mattress, if appropriate / needed. |
| Q24 | varchar |  |  | SI | If a wound is present commence wound assessment sh... |
| Q25 | varchar |  |  | SI | Reassess twice daily or more frequently if conditi... |
| Q26 | varchar |  |  | SI | 11 to 19: High risk |
| Q27 | varchar |  |  | SI | Seek advice from the tissue viability link nurses ... |
| Q28 | varchar |  |  | SI | Implement regular position and equipment pressure ... |
| Q29 | varchar |  |  | SI | Use gel mattress, if appropriate / needed. |
| Q30 | varchar |  |  | SI | If a wound is present, commence wound assessment s... |
| Q31 | varchar |  |  | SI | Reassess daily or as condition changes. |
| Q32 | varchar |  |  | SI | 6 to 10: At risk |
| Q33 | varchar |  |  | SI | Commence tissue viability care plan. |
| Q34 | varchar |  |  | SI | Reassess twice weekly or as condition changes. |
| Q35 | varchar |  |  | SI | 0 to 5: Low risk |
| Q36 | varchar |  |  | SI | Reassess weekly or as condition changes. |
| Q37 | varchar |  |  | SI | Ashworth C, Briggs L. Design and implementation of... |
| Q38 | varchar |  |  | SI | The Neonatal Tissue Viability Risk Assessment Tool... |
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