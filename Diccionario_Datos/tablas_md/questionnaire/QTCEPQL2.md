# questionnaire.QTCEPQL2

> Instrumento Medición Calidad de Vida Pacientes con Asma (5-7 Años): Informe de Padres

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Instrumento Medición Calidad de Vida Pacientes con Asma (5-7 Años): Informe de Padres

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1 Dolor o sensacion de pecho apretado |
| Q02 | varchar |  |  | SI | 2.Sensación de ruidos al respirar |
| Q03 | varchar |  |  | SI | 3. Haber tenido ataques de asma |
| Q04 | varchar |  |  | SI | 4. Estar asustado mientras tiene un ataque de asma |
| Q05 | varchar |  |  | SI | 5. Ahogarse |
| Q06 | varchar |  |  | SI | 6. Tener tos |
| Q07 | varchar |  |  | SI | 7. Para respirar profundo |
| Q08 | varchar |  |  | SI | 8. Tener la nariz tapada o con romadizo (moco) |
| Q09 | varchar |  |  | SI | 9. Despertar en la noche con dificultad para respi... |
| Q10 | varchar |  |  | SI | 10. Jugar con mascotas |
| Q11 | varchar |  |  | SI | 11. Jugar en el exterior de la casa |
| Q12 | varchar |  |  | SI | 1. El tratamiento le hace sentir mal |
| Q13 | varchar |  |  | SI | 2. Dificultad para dormir por su tratamiento  |
| Q14 | varchar |  |  | SI | 3. Problemas al usar su inhalador |
| Q15 | varchar |  |  | SI | 4. No le agrada andar con su inhalador |
| Q16 | varchar |  |  | SI | 5. No le agrada hacerse responsable de sus medicam... |
| Q17 | varchar |  |  | SI | 6. Controlar su asma |
| Q18 | varchar |  |  | SI | 7. Se niega a tomar o usar  sus medicamentos |
| Q19 | varchar |  |  | SI | 8. Se olvida de tomar su tratamiento |
| Q20 | varchar |  |  | SI | 9. Se pone nervioso cuando tiene que tomarse o usa... |
| Q21 | varchar |  |  | SI | 10. Se pone nervioso al tener que ir al médico |
| Q22 | varchar |  |  | SI | 11. Se pone nervioso cuando debe hospitalizarse |
| Q23 | varchar |  |  | SI | 1. Preocupación por problemas indeseables de su tr... |
| Q24 | varchar |  |  | SI | 2. Preocupación si su tratamiento no le está hacie... |
| Q25 | varchar |  |  | SI | 3. Preocupación por su asma |
| Q26 | varchar |  |  | SI | 1. Decirle al doctor, enfermera o kinesiólogo como... |
| Q27 | varchar |  |  | SI | 2. Hacerle preguntas al doctor, enfermera o kinesi... |
| Q28 | varchar |  |  | SI | 3. Explicarle su enfermedad a los demás |
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