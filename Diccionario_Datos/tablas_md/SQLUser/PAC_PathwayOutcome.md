# SQLUser.PAC_PathwayOutcome

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPO_ParRef | bigint | PK |  | NO | Parent Reference |
| PACPO_Childsub | double |  |  | NO | Childsub |
| PACPO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACPO_CreatedDate | date |  |  | SI | Created Date |
| PACPO_CreatedTime | time |  |  | SI | Created Time |
| PACPO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPO_Outcome_DR | bigint |  | FK | SI | Protocol Outcome |
| PACPO_RowId | varchar |  |  | NO | - |
| PACPO_UpdatedDate | date |  |  | SI | Updated Date |
| PACPO_UpdatedTime | time |  |  | SI | Updated Time |
| PACPO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Intensity and duration of pressure |
| Q04 | - |  |  | SI | General physical condition |
| Q05 | - |  |  | SI | Mobility |
| Q06 | - |  |  | SI | Activity |
| Q07 | - |  |  | SI | Sensory perception |
| Q08 | - |  |  | SI | Tolerance of the skin and supporting structure |
| Q09 | - |  |  | SI | Moisture |
| Q10 | - |  |  | SI | Friction |
| Q11 | - |  |  | SI | Nutrition |
| Q12 | - |  |  | SI | Tissue perfusion and oxygenation |
| Q13 | - |  |  | SI | Definitions |
| Q14 | - |  |  | SI | Mobility: The ability to change and control body p... |
| Q15 | - |  |  | SI | Activity: The degree of physical activity.	 |
| Q16 | - |  |  | SI | Sensory perception: The ability to respond in a de... |
| Q17 | - |  |  | SI | Moisture: Degree to which skin is exposed to moist... |
| Q18 | - |  |  | SI | Friction: (ie babies on CPAP).	 |
| Q19 | - |  |  | SI | Nutrition: Usual milk / fluid intake pattern. |
| Q20 | - |  |  | SI | 20 or over: Very high risk |
| Q21 | - |  |  | SI | Refer to tissue viability link nurses / specialist... |
| Q22 | - |  |  | SI | Implement regular position regular position change... |
| Q23 | - |  |  | SI | Use gel mattress, if appropriate / needed. |
| Q24 | - |  |  | SI | If a wound is present commence wound assessment sh... |
| Q25 | - |  |  | SI | Reassess twice daily or more frequently if conditi... |
| Q26 | - |  |  | SI | 11 to 19: High risk |
| Q27 | - |  |  | SI | Seek advice from the tissue viability link nurses ... |
| Q28 | - |  |  | SI | Implement regular position and equipment pressure ... |
| Q29 | - |  |  | SI | Use gel mattress, if appropriate / needed. |
| Q30 | - |  |  | SI | If a wound is present, commence wound assessment s... |
| Q31 | - |  |  | SI | Reassess daily or as condition changes. |
| Q32 | - |  |  | SI | 6 to 10: At risk |
| Q33 | - |  |  | SI | Commence tissue viability care plan. |
| Q34 | - |  |  | SI | Reassess twice weekly or as condition changes. |
| Q35 | - |  |  | SI | 0 to 5: Low risk |
| Q36 | - |  |  | SI | Reassess weekly or as condition changes. |
| Q37 | - |  |  | SI | Ashworth C, Briggs L. Design and implementation of... |
| Q38 | - |  |  | SI | The Neonatal Tissue Viability Risk Assessment Tool... |
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