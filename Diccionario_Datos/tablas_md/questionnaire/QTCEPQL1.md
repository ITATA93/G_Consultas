# questionnaire.QTCEPQL1

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | 1. Dolor o sensación de pecho apretado |
| Q02 | varchar | PK |  | SI | 2. Sensación de ruidos al respirar |
| Q03 | varchar | PK |  | SI | 3. Haber tenido ataques de asma |
| Q04 | varchar | PK |  | SI | 4. Estar asustado cuando tiene ataques de asma |
| Q05 | varchar | PK |  | SI | 5. Ahogarse |
| Q06 | varchar | PK |  | SI | 6. Tener tos |
| Q07 | varchar | PK |  | SI | 7. Al hacer inspiraciones profundas |
| Q08 | varchar | PK |  | SI | 8. Tener nariz tapada o con secreciones |
| Q09 | varchar | PK |  | SI | 9. Al despertar en la noche con problemas para res... |
| Q10 | varchar | PK |  | SI | 10. Al jugar con mascotas |
| Q11 | varchar | PK |  | SI | 11. Al jugar al aire libre |
| Q12 | varchar | PK |  | SI | 1. Su tratamiento le hace sentir mal |
| Q13 | varchar | PK |  | SI | 2. Su tratamiento le da sueño |
| Q14 | varchar | PK |  | SI | 3. El uso de sus inhaladores le da problema |
| Q15 | varchar | PK |  | SI | 4. No le gusta andar trayendo su inhalador |
| Q16 | varchar | PK |  | SI | 5. No le agrada tener que tomar o usar medicamento... |
| Q17 | varchar | PK |  | SI | 6. Se olvida tomar sus medicamentos |
| Q18 | varchar | PK |  | SI | 7. Se pone nervioso al tener que usar su tratamien... |
| Q19 | varchar | PK |  | SI | 8. Se pone nervioso al tener que ir al médico |
| Q20 | varchar | PK |  | SI | 9. Se pone nervioso al tener que ir al hospoital |
| Q21 | varchar | PK |  | SI | 1. Preocupado por efectos adversos o indeseables d... |
| Q22 | varchar | PK |  | SI | 2. Preocupado por si sus medicamentos le hacen o n... |
| Q23 | varchar | PK |  | SI | 3. Preocupado por su asma |
| Q24 | varchar | PK |  | SI | 1. Decirle a si médico , enfermera o Kinesiólogo c... |
| Q25 | varchar | PK |  | SI | 2. Hacerle preguntas al médico, enfermera o kinesi... |
| Q26 | varchar | PK |  | SI | 3. Explicarle a los demás su enfermedad |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*