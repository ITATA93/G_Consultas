# questionnaire.QCLXXTSK

> Escala de Tampa para Kinesiofobia (TSK)

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Tampa para Kinesiofobia (TSK)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | INSTRUCCIONES: se enumeran una serie de afirmacion... |
| Q02 | varchar |  |  | SI | Totalmente en Desacuerdo |
| Q03 | varchar |  |  | SI | Totalmente de acuerdo |
| Q04 | varchar |  |  | SI | 1 = Totalmente en desacuerdo |
| Q05 | varchar |  |  | SI | 2 = Algo en desacuerdo |
| Q06 | varchar |  |  | SI | 3 = Parcialmente de acuerdo |
| Q07 | varchar |  |  | SI | 4 = Totalmente de acuerdo |
| Q08 | varchar |  |  | SI | CUESTIONARIO TSK-11SV |
| Q09 | varchar |  |  | SI | Escala de Tampa para Kinesiofobia |
| Q10 | varchar |  |  | SI | 1. Tengo miedo de lesionarme si hago ejercicio fís... |
| Q11 | varchar |  |  | SI | 2. Si me dejara vencer por el dolor, el dolor aume... |
| Q12 | varchar |  |  | SI | 3. Mi cuerpo me está diciendo que tengo algo serio... |
| Q13 | varchar |  |  | SI | 4. Tener dolor siempre quiere decir que en el cuer... |
| Q14 | varchar |  |  | SI | 5. Tengo miedo a lesionarme sin querer. |
| Q15 | varchar |  |  | SI | 6. Lo más seguro para evitar que aumente el dolor ... |
| Q16 | varchar |  |  | SI | 7. No me dolería tanto si no tuviese algo serio en... |
| Q17 | varchar |  |  | SI | 8. El dolor me dice cuándo debo parar la actividad... |
| Q18 | varchar |  |  | SI | 9. No es seguro para una persona con mi enfermedad... |
| Q19 | varchar |  |  | SI | 10. No puedo hacer todo lo que la gente normal hac... |
| Q20 | varchar |  |  | SI | 11. Nadie debería hacer actividades físicas cuando... |
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