# questionnaire.QTCEPRPSICO

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | 1- Ingreso a control prenatal posterior a las 20 s... |
| Q02 | varchar | PK |  | SI | 2- Escolaridad menor a sexto básico |
| Q03 | varchar | PK |  | SI | 3- Edad menor a 17 años y 11 meses |
| Q04 | varchar | PK |  | SI | 4- Rechazo al Embarazo |
| Q05 | varchar | PK |  | SI | 5- Insuficiente apoyo social o familiar |
| Q06 | varchar | PK |  | SI | 6- Sintomas depresivos, por más de dos semanas |
| Q07 | varchar | PK |  | SI | 7- Uso a abuso de sustancias |
| Q08 | varchar | PK |  | SI | 8- Violencia, pareja u otra figura masculina |
| Q09 | varchar | PK |  | SI | 9- ¿Hay algún otro factor de riesgo que deba ser c... |
| Q10 | varchar | PK |  | SI | Observaciones |
| Q11 | varchar | PK |  | SI | Especifique |
| Q12 | varchar | PK |  | SI | Especifique |
| Q13 | varchar | PK |  | SI | ¿Ha pensado en interrumpir la gestación? o ¿Prefer... |
| Q14 | varchar | PK |  | SI | Marque SI, sí pensó en interrumpir o aún se siente... |
| Q15 | varchar | PK |  | SI | (pareja, familia u otra figura significativa que a... |
| Q16 | varchar | PK |  | SI | ¿Se siente insatisfecha con el apoyo de la familia... |
| Q17 | varchar | PK |  | SI | Marque SI, sí siente que no cuenta con el apoyo ne... |
| Q18 | varchar | PK |  | SI | A- Cigarrillo B- Cerveza, vino, trago fuerte u otr... |
| Q19 | varchar | PK |  | SI | Marque SI, sí ha consumido cualquiera de otras sus... |
| Q20 | varchar | PK |  | SI | A- ¿Alguien la ha insultado, humillado o amenazado... |
| Q21 | varchar | PK |  | SI | B- ¿Le controlan con quien conversa o sus actos? (... |
| Q22 | varchar | PK |  | SI | C- ¿Alguien la ha golpeado o empujado? (VIOLENCIA ... |
| Q23 | varchar | PK |  | SI | D- ¿Este embarazo es consecuencia de una relación ... |
| Q24 | varchar | PK |  | SI | Marque SI, sí ha sucedido cualquiera de estas mani... |
| Q25 | varchar | PK |  | SI | En el caso que la fuente de violencia sea alguien ... |
| Q26 | varchar | PK |  | SI | Que no esté señalado en los anteriores. Considerar... |
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