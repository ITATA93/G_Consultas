# questionnaire.QTCEPQL7

> Instrumento Medición Calidad de Vida Pacientes con Asma (13-18 Años): Reporte de Adolescentes

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Instrumento Medición Calidad de Vida Pacientes con Asma (13-18 Años): Reporte de Adolescentes

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Me duele el pecho o lo siento apretado |
| Q02 | varchar |  |  | SI | 2. Me silba el pecho o tengo ruidos al respirar |
| Q03 | varchar |  |  | SI | 3. Tengo ataques de asma |
| Q04 | varchar |  |  | SI | 4. Me asusto cuando tengo ataques de asma |
| Q05 | varchar |  |  | SI | 5. Me canso |
| Q06 | varchar |  |  | SI | 6. Tengo tos |
| Q07 | varchar |  |  | SI | 7. Me cuesta respirar profundo |
| Q08 | varchar |  |  | SI | 8. Se me tapa la nariz o me da romadizo (moco) |
| Q09 | varchar |  |  | SI | 9. Despierto en la noche con dificultad para respi... |
| Q10 | varchar |  |  | SI | 10. Me cuesta jugar con mascotas |
| Q11 | varchar |  |  | SI | 11. Me cuesta jugar fuera de mi casa |
| Q12 | varchar |  |  | SI | 1. Mis medicamentos me hacen sentir mal |
| Q13 | varchar |  |  | SI | 2. Mis medicamentos me dan problemas para dormir |
| Q14 | varchar |  |  | SI | 3. Tengo problemas para usar mi inhalador |
| Q15 | varchar |  |  | SI | 4. No me gusta andar con mi inhalador |
| Q16 | varchar |  |  | SI | 5. Me cuesta hacerme responsable de mis medicament... |
| Q17 | varchar |  |  | SI | 6. Es dificil para mi controlar mi asma |
| Q18 | varchar |  |  | SI | 7. Me niego a tomarme mis medicamentos |
| Q19 | varchar |  |  | SI | 8. Me olvido de usar o tomarme mis medicamentos |
| Q20 | varchar |  |  | SI | 9. Me asusto cuando tengo que usar mis medicamento... |
| Q21 | varchar |  |  | SI | 10. Me asusto cuando debo ir al médico |
| Q22 | varchar |  |  | SI | 11. Me asusto cuando tengo que ir a hospitalizarme |
| Q23 | varchar |  |  | SI | 1. Me preocupan los efectos indeseables de mis med... |
| Q24 | varchar |  |  | SI | 2. Me preocupo por si mi tratamiento no me está ha... |
| Q25 | varchar |  |  | SI | 3. Me preocupa mi asma |
| Q26 | varchar |  |  | SI | 1. Me cuesta decirle al médico, enfermera o kinesi... |
| Q27 | varchar |  |  | SI | 2. Me cuesta hacerle preguntas al médico, enfermer... |
| Q28 | varchar |  |  | SI | 3. Me cuesta explicarle mi enfermedad a los demas |
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