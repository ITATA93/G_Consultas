# questionnaire.QTCEEZARIT2

> Test de Zarit

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Test de Zarit

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre Cuidador |
| Q02 | varchar |  |  | SI | RUN |
| Q03 | varchar |  |  | SI | Parentesco |
| Q04 | varchar |  |  | SI | ¿Piensa que su familiar le pide más ayuda de la qu... |
| Q05 | varchar |  |  | SI | ¿Piensa que debido al tiempo que dedica a su famil... |
| Q06 | varchar |  |  | SI | ¿Se siente agobiado por intentar compatibilizar el... |
| Q07 | varchar |  |  | SI | ¿Siente vergüenza por la conducta de su familiar? |
| Q08 | varchar |  |  | SI | ¿Se siente enfadado cuando esta cerca de su famili... |
| Q09 | varchar |  |  | SI | ¿Piensa que el cuidar de su familiar afecta negati... |
| Q10 | varchar |  |  | SI | ¿Tiene miedo por el futuro de su familiar? |
| Q11 | varchar |  |  | SI | ¿Piensa que su familiar depende de Ud.? |
| Q12 | varchar |  |  | SI | ¿Se siente tenso cuando está cerca de su familiar? |
| Q13 | varchar |  |  | SI | ¿Piensa que su salud ha empeorado debido a tener q... |
| Q14 | varchar |  |  | SI | ¿Piensa que no tiene tanta intimidad como le gusta... |
| Q15 | varchar |  |  | SI | ¿Piensa que su vida social se ha visto afectada ne... |
| Q16 | varchar |  |  | SI | ¿Se siente incómodo por distanciarse de sus amista... |
| Q17 | varchar |  |  | SI | ¿Piensa que su familiar le considera a usted la ún... |
| Q18 | varchar |  |  | SI | ¿Piensa que no tiene suficientes ingresos económic... |
| Q19 | varchar |  |  | SI | ¿Piensa que no será capaz de cuidar a su familiar ... |
| Q20 | varchar |  |  | SI | ¿Se siente que ha perdido el control de su vida de... |
| Q21 | varchar |  |  | SI | ¿Desearía poder dejar el cuidado de su familiar a ... |
| Q22 | varchar |  |  | SI | ¿Se siente indeciso sobre qué hacer con su familia... |
| Q23 | varchar |  |  | SI | ¿Piensa que debería hacer más por su familiar ? |
| Q24 | varchar |  |  | SI | ¿Piensa que podría cuidar mejor a su familiar? |
| Q25 | varchar |  |  | SI | Globalmente, ¿qué grado de carga experimenta por e... |
| QRES | varchar |  |  | SI | Resultado Test Zarit |
| QRESObsDR | varchar |  | FK | SI | Resultado Test Zarit DR |
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