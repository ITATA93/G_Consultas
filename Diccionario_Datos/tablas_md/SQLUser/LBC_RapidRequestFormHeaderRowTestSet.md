# SQLUser.LBC_RapidRequestFormHeaderRowTestSet

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRRFHRTS_ParRef | varchar | PK |  | NO | Parent table |
| LBCRRFHRTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRRFHRTS_Colour | varchar |  |  | SI | Colour |
| LBCRRFHRTS_RowID | varchar |  |  | NO | - |
| LBCRRFHRTS_Sequence | integer |  |  | SI | Sequence |
| LBCRRFHRTS_Superset_DR | bigint |  | FK | SI | Superset |
| LBCRRFHRTS_TestSet_DR | bigint |  | FK | SI | Test Set |
| Q01 | - |  |  | SI | 1 Dolor o sensacion de pecho apretado |
| Q02 | - |  |  | SI | 2.Sensación de ruidos al respirar |
| Q03 | - |  |  | SI | 3. Haber tenido ataques de asma |
| Q04 | - |  |  | SI | 4. Estar asustado mientras tiene un ataque de asma |
| Q05 | - |  |  | SI | 5. Ahogarse |
| Q06 | - |  |  | SI | 6. Tener tos |
| Q07 | - |  |  | SI | 7. Para respirar profundo |
| Q08 | - |  |  | SI | 8. Tener la nariz tapada o con romadizo (moco) |
| Q09 | - |  |  | SI | 9. Despertar en la noche con dificultad para respi... |
| Q10 | - |  |  | SI | 10. Jugar con mascotas |
| Q11 | - |  |  | SI | 11. Jugar en el exterior de la casa |
| Q12 | - |  |  | SI | 1. El tratamiento le hace sentir mal |
| Q13 | - |  |  | SI | 2. Dificultad para dormir por su tratamiento |
| Q14 | - |  |  | SI | 3. Problemas al usar su inhalador |
| Q15 | - |  |  | SI | 4. No le agrada andar con su inhalador |
| Q16 | - |  |  | SI | 5. No le agrada hacerse responsable de sus medicam... |
| Q17 | - |  |  | SI | 6. Controlar su asma |
| Q18 | - |  |  | SI | 7. Se niega a tomar o usar  sus medicamentos |
| Q19 | - |  |  | SI | 8. Se olvida de tomar su tratamiento |
| Q20 | - |  |  | SI | 9. Se pone nervioso cuando tiene que tomarse o usa... |
| Q21 | - |  |  | SI | 10. Se pone nervioso al tener que ir al médico |
| Q22 | - |  |  | SI | 11. Se pone nervioso cuando debe hospitalizarse |
| Q23 | - |  |  | SI | 1. Preocupación por problemas indeseables de su tr... |
| Q24 | - |  |  | SI | 2. Preocupación si su tratamiento no le está hacie... |
| Q25 | - |  |  | SI | 3. Preocupación por su asma |
| Q26 | - |  |  | SI | 1. Decirle al doctor, enfermera o kinesiólogo como... |
| Q27 | - |  |  | SI | 2. Hacerle preguntas al doctor, enfermera o kinesi... |
| Q28 | - |  |  | SI | 3. Explicarle su enfermedad a los demás |
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