# SQLUser.PAC_DefTreatmentInitiator

**Schema:** SQLUser
**Columnas:** 149
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DFTI_RowId | bigint | PK |  | NO | - |
| DFTI_Code | varchar |  |  | NO | Code |
| DFTI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DFTI_CreatedDate | date |  |  | SI | Created Date |
| DFTI_CreatedTime | time |  |  | SI | Created Time |
| DFTI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DFTI_DateFrom | date |  |  | SI | DateFrom |
| DFTI_DateTo | date |  |  | SI | DateTo |
| DFTI_DefAdmDueDateApply | varchar |  |  | SI | Deferred Admission due date to be applied |
| DFTI_Desc | varchar |  |  | NO | Description |
| DFTI_Owner | varchar |  |  | SI | Owner |
| DFTI_ReCalculateWaitTime | varchar |  |  | SI | ReCalculateWaitTime |
| DFTI_UpdatedDate | date |  |  | SI | Updated Date |
| DFTI_UpdatedTime | time |  |  | SI | Updated Time |
| DFTI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Deberá responder a estas preguntas pensando en los... |
| Q04 | - |  |  | SI | últimos siete días. |
| Q05 | - |  |  | SI | S1. ¿Tuvo hinchazón en la rodilla? |
| Q06 | - |  |  | SI | S2. ¿Sentía fricción o escuchó algún sonido o ruid... |
| Q07 | - |  |  | SI | S3. ¿Su rodilla se trababa o quedaba colgada cuand... |
| Q08 | - |  |  | SI | S4. ¿Podía enderezar totalmente su rodilla? |
| Q09 | - |  |  | SI | S5. ¿Podía doblar totalmente su rodilla? |
| Q10 | - |  |  | SI | Las siguientes preguntas son en relación a la inte... |
| Q11 | - |  |  | SI | últimos siete días |
| Q12 | - |  |  | SI | en su rodilla. Rigidez es la sensación de restricc... |
| Q13 | - |  |  | SI | S6. ¿Qué tan severa fue la rigidez en su rodilla a... |
| Q14 | - |  |  | SI | S7. En el transcurso del día, ¿qué tan severa ha s... |
| Q15 | - |  |  | SI | P1. ¿Con qué frecuencia ha sentido usted dolor en ... |
| Q16 | - |  |  | SI | ¿Cuánto dolor ha sentido en su rodilla en los |
| Q17 | - |  |  | SI | &nbsp |
| Q18 | - |  |  | SI | durante las siguientes actividades? |
| Q19 | - |  |  | SI | P2. Torciendo/rotando su rodilla |
| Q20 | - |  |  | SI | P3. Enderezando totalmente su rodilla |
| Q21 | - |  |  | SI | P4. Doblando totalmente su rodilla |
| Q22 | - |  |  | SI | P5. Al caminar en una superficie plana |
| Q23 | - |  |  | SI | P6. Al subir o bajar escaleras |
| Q24 | - |  |  | SI | P7. Por la noche, al estar en la cama |
| Q25 | - |  |  | SI | P8. Al estar sentado(a) o recostado(a) |
| Q26 | - |  |  | SI | P9. Al estar de pie |
| Q27 | - |  |  | SI | Las siguientes preguntas se refieren a su funciona... |
| Q28 | - |  |  | SI | dificultad que ha sentido en su funcionamiento fís... |
| Q29 | - |  |  | SI | últimos siete días |
| Q30 | - |  |  | SI | debido a su rodilla afectada. |
| Q31 | - |  |  | SI | A1. Al bajar las escaleras |
| Q32 | - |  |  | SI | A2. Al subir las escaleras |
| Q33 | - |  |  | SI | Para cada una de las siguientes actividades, por f... |
| Q34 | - |  |  | SI | últimos siete días |
| Q35 | - |  |  | SI | debido a su rodilla afectada. |
| Q36 | - |  |  | SI | A3. Al levantarse después de estar sentado(a) |
| Q37 | - |  |  | SI | A4. Al estar de pie |
| Q38 | - |  |  | SI | A5. Al agacharse en cuclillas a recoger un objeto ... |
| Q39 | - |  |  | SI | A6. Al caminar en una superficie plana |
| Q40 | - |  |  | SI | A7. Al subirse o bajarse de un carro |
| Q41 | - |  |  | SI | A8. Al ir de compras |
| Q42 | - |  |  | SI | A9. Al ponerse los calcetines o las medias |
| Q43 | - |  |  | SI | A10. Al levantarse de la cama |
| Q44 | - |  |  | SI | A12. Al estar recostado(a) en la cama (cuando se v... |
| Q45 | - |  |  | SI | A13. Al entrar o salir de la tina (bañadera) |
| Q46 | - |  |  | SI | A14. Al estar sentado(a) |
| Q47 | - |  |  | SI | A15. Al sentarse o levantarse del inodoro [excusad... |
| Q48 | - |  |  | SI | Para cada una de las siguientes actividades, por f... |
| Q49 | - |  |  | SI | últimos siete días |
| Q50 | - |  |  | SI | debido a su rodilla afectada. |
| Q51 | - |  |  | SI | A16. Trabajo pesado en la casa (moviendo cajas pes... |
| Q52 | - |  |  | SI | A17. Trabajo liviano en la casa (cocinando, desemp... |
| Q53 | - |  |  | SI | Las siguientes preguntas se refieren al funcionami... |
| Q54 | - |  |  | SI | últimos siete días |
| Q55 | - |  |  | SI | debido a su rodilla. |
| Q56 | - |  |  | SI | SP1. Sentándose en cuclillas |
| Q57 | - |  |  | SI | SP2. Corriendo |
| Q58 | - |  |  | SI | SP3. Saltando |
| Q59 | - |  |  | SI | SP4. Torciendo/rotando en su rodilla afectada |
| Q60 | - |  |  | SI | SP5. Arrodillándose |
| Q61 | - |  |  | SI | Q1. ¿Con qué frecuencia está conciente del problem... |
| Q62 | - |  |  | SI | Q2. ¿Ha cambiado su estilo de vida para evitar act... |
| Q63 | - |  |  | SI | Q3. ¿Qué tanto le preocupa la falta de confianza e... |
| Q64 | - |  |  | SI | Q4. Generalmente, ¿cuánta dificultad tiene con su ... |
| Q65 | - |  |  | SI | Puntaje Dolor |
| Q66 | - |  |  | SI | Puntaje Síntomas |
| Q67 | - |  |  | SI | Puntaje Actividades Cotidianas |
| Q68 | - |  |  | SI | Puntaje&nbsp |
| Q69 | - |  |  | SI | Puntaje de Calidad de Vida |
| Q70 | - |  |  | SI | &gt |
| Q71 | - |  |  | SI | 100 indica que no hay problemas y 0 indica problem... |
| Q72 | - |  |  | SI | Cada elemento se califica de 0 a 4, donde 0 repres... |
| Q73 | - |  |  | SI | Responda al menos la mitad de los ítems de la esca... |
| Q74 | - |  |  | SI | Las puntuaciones de la escala KOOS se transforman ... |
| Q75 | - |  |  | SI | 100 indica que no hay problemas |
| Q76 | - |  |  | SI | y |
| Q77 | - |  |  | SI | 0 indica problemas extremos. |
| Q78 | - |  |  | SI | Puntaje |
| Q79 | - |  |  | SI | Clasificación |
| Q80 | - |  |  | SI | 100 |
| Q81 | - |  |  | SI | Indica que no hay problemas |
| Q82 | - |  |  | SI | 0 |
| Q83 | - |  |  | SI | Indica problemas extremos |
| Q84 | - |  |  | SI | La puntuación de resultados de lesiones de rodilla... |
| Q85 | - |  |  | SI | 100: indica que no hay problemas |
| Q86 | - |  |  | SI | 0: Indica problemas extremos |
| Q87 | - |  |  | SI | A11. Al quitarse los calcetines o las medias |
| Q88 | - |  |  | SI | 0 - 100: la puntuación que va de 0 indica problema... |
| Q89 | - |  |  | SI | 0 - 100 |
| Q90 | - |  |  | SI | La puntuación que va desde 0 indica problemas extr... |
| Q91 | - |  |  | SI | Ewa M. Roos, Harald P. Roos, L. Stefan Lohmander, ... |
| Q92 | - |  |  | SI | Development of a Self-Administered Outcome Measure... |
| Q93 | - |  |  | SI | https://www.jospt.org/doi/10.2519/jospt.1998.28.2.... |
| Q94 | - |  |  | SI | http://www.koos.nu/ |
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