# questionnaire.QCLXXPEMRSU

> Pauta para la Evaluación y Manejo del Riesgo Suicida (en base a Columbia)

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pauta para la Evaluación y Manejo del Riesgo Suicida (en base a Columbia)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1) ¿Has deseado estar muerto(a) o poder dormirte y... |
| Q02 | varchar |  |  | SI | La persona confirma que ha tenido ideas relacionad... |
| Q03 | varchar |  |  | SI | 2) ¿Has tenido realmente la idea de suicidarte? |
| Q04 | varchar |  |  | SI | Pensamientos generales y no específicos relativos ... |
| Q05 | varchar |  |  | SI | Si la respuesta es “SÍ” a la pregunta 2, formule l... |
| Q06 | varchar |  |  | SI | Si la respuesta es “NO” continúe a la pregunta 6 |
| Q07 | varchar |  |  | SI | 3) ¿Has pensado en cómo llevarías esto a cabo? |
| Q08 | varchar |  |  | SI | El o la estudiante confirma que ha tenido ideas su... |
| Q09 | varchar |  |  | SI | un método para matarse, pero sin un plan específic... |
| Q10 | varchar |  |  | SI | realmente...y nunca lo haría”. |
| Q11 | varchar |  |  | SI | 4) ¿Has tenido estas ideas y en cierto grado la in... |
| Q12 | varchar |  |  | SI | Se presentan ideas suicidas activas de quitarse la... |
| Q13 | varchar |  |  | SI | “Tengo los pensamientos, pero definitivamente no h... |
| Q14 | varchar |  |  | SI | 5) ¿Has comenzado a elaborar o has elaborado los d... |
| Q15 | varchar |  |  | SI | Se presentan ideas de quitarse la vida con detalle... |
| Q16 | varchar |  |  | SI | Siempre realice la pregunta 6 |
| Q17 | varchar |  |  | SI | 6) ¿Alguna vez has hecho algo, comenzado a hacer a... |
| Q18 | varchar |  |  | SI | Pregunta de conducta suicida: Ejemplos: ¿Has junta... |
| Q19 | varchar |  |  | SI | ¿has sacado remedios del frasco o caja, pero no la... |
| Q20 | varchar |  |  | SI | o ¿realmente has tomado remedios, has tratado de d... |
| Q21 | varchar |  |  | SI | Si la respuesta es “SI”: ¿Fue dentro de los último... |
| Q22 | varchar |  |  | SI | Toma de Decisiones para el facilitador comunitario... |
| Q23 | varchar |  |  | SI | Si el estudiante responde que NO a todas las pregu... |
| Q24 | varchar |  |  | SI | Si la respuesta fue Sí sólo a las preguntas 1 y 2: |
| Q25 | varchar |  |  | SI | Riesgo Bajo |
| Q26 | varchar |  |  | SI | 1) Informe al Área de Convivencia sobre el riesgo ... |
| Q27 | varchar |  |  | SI | 2) Contacte a los padres o cuidadores y sugiera ac... |
| Q28 | varchar |  |  | SI | 3) Entregue ficha de derivación a centro de salud ... |
| Q29 | varchar |  |  | SI | 4) Realice seguimiento del/la estudiante. |
| Q30 | varchar |  |  | SI | Si la respuesta fue Sí a pregunta 3 o “más allá de... |
| Q31 | varchar |  |  | SI | Riesgo Medio |
| Q32 | varchar |  |  | SI | 1) Informe al Director una vez finalizada la entre... |
| Q33 | varchar |  |  | SI | 2) Una vez informado, el Director (o a quien éste ... |
| Q34 | varchar |  |  | SI | 3) Entregue a los padres la ficha de derivación al... |
| Q35 | varchar |  |  | SI | 4) Realice seguimiento del caso, asegurándose que ... |
| Q36 | varchar |  |  | SI | 5) Recomiende medidas de seguridad en caso de que ... |
| Q37 | varchar |  |  | SI | Si la respuesta fue Sí a preguntas 4, 5 y/o 6 en l... |
| Q38 | varchar |  |  | SI | Riesgo Alto |
| Q39 | varchar |  |  | SI | 1) Informe al Director |
| Q40 | varchar |  |  | SI | 2) Una vez informado, el Director (o a quien éste ... |
| Q41 | varchar |  |  | SI | acompañen al estudiante y que éste concurra a aten... |
| Q42 | varchar |  |  | SI | En caso de encontrarse fuera de horario de atenció... |
| Q43 | varchar |  |  | SI | 3) Tome medidas de precaución inmediatas para el r... |
| Q44 | varchar |  |  | SI | • Acompañar al estudiante hasta que se encuentre c... |
| Q45 | varchar |  |  | SI | • Facilitar la coordinación con el Centro de Atenc... |
| Q46 | varchar |  |  | SI | • Eliminar medios letales del entorno |
| Q47 | varchar |  |  | SI | Último mes |
| Q48 | varchar |  |  | SI | Alguna vez en la vida |
| Q49 | varchar |  |  | SI | En los últimos 3 meses |
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