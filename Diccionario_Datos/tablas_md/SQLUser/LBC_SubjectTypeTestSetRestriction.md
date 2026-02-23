# SQLUser.LBC_SubjectTypeTestSetRestriction

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSUBTR_ParRef | bigint | PK |  | NO | Parent table |
| LBCSUBTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSUBTR_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| LBCSUBTR_RowID | varchar |  |  | NO | - |
| LBCSUBTR_Superset_DR | bigint |  | FK | SI | Referring Hospital |
| LBCSUBTR_TestSet_DR | bigint |  | FK | SI | Location |
| Q01 | - |  |  | SI | 1. Dolor o pecho apretado |
| Q02 | - |  |  | SI | 2. Respiración ruidosa o pecho que silba |
| Q03 | - |  |  | SI | 3. Ha tenido ataques de asma |
| Q04 | - |  |  | SI | 4. Asustado mientras tiene un ataque de asma |
| Q05 | - |  |  | SI | 5. Falta de aire o cansancio |
| Q06 | - |  |  | SI | 6. Tos |
| Q07 | - |  |  | SI | 7. Al respirar profundo |
| Q08 | - |  |  | SI | 8. Tener la nariz tapada o con secreción nasal (mo... |
| Q09 | - |  |  | SI | 9. Despertar en la noche con problemas para respir... |
| Q10 | - |  |  | SI | 10. Jugar con mascotas |
| Q11 | - |  |  | SI | 11. Jugar fuera de la casa |
| Q12 | - |  |  | SI | 1. El tratamiento le hace sentir mal |
| Q13 | - |  |  | SI | 2. El tratamiento le produce dificultad para dormi... |
| Q14 | - |  |  | SI | 3. Tiene dificultad para usar su inhalador |
| Q15 | - |  |  | SI | 4. No le agrada llevar consigo su inhalador |
| Q16 | - |  |  | SI | 5. Tiene problemas para hacerse responsable de sus... |
| Q17 | - |  |  | SI | 6. Para controlar su asma |
| Q18 | - |  |  | SI | 7. Rechaza hacer el tratamiento |
| Q19 | - |  |  | SI | 8. Se olvida de usar sus medicamentos |
| Q20 | - |  |  | SI | 9. Se pone nervioso cuando tiene que hacer su trat... |
| Q21 | - |  |  | SI | 10. Se pone nervioso cuando tiene que ir al médico |
| Q22 | - |  |  | SI | 11. Se pone nervioso cuando tiene que hospitalizar... |
| Q23 | - |  |  | SI | 1. Preocupación por problemas indeseales de su tra... |
| Q24 | - |  |  | SI | 2. Preocupación si su tratamiento le está haciendo... |
| Q25 | - |  |  | SI | 3. Para hacerle preguntas al mérico, enfermera o k... |
| Q26 | - |  |  | SI | 4. Al explicar su enfermedad a los demás |
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