# questionnaire.QTCEFRP

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| QAC | varchar | PK |  | SI | Actividades compartidas |
| QADMSRSF | varchar | PK |  | SI | Adultos mayores sin red social y familiar |
| QAOHDMF | varchar | PK |  | SI | Abuso de Alcohol Drogras de algún miembro de la Fa... |
| QAS | varchar | PK |  | SI | ¿Aislamiento social? |
| QBCF | varchar | PK |  | SI | Buena comunicación familiar |
| QBEMPS | varchar | PK |  | SI | Baja escolaridad Madre, Padre o Sustituto (Básica ... |
| QCD | varchar | PK |  | SI | Controles al día |
| QDDPSIMF | varchar | PK |  | SI | Déficit Desarrollo Psicomotor de un miembro de la ... |
| QDEPMF | varchar | PK |  | SI | Depresión de Agún miembro de la Familia |
| QEAF | varchar | PK |  | SI | Expresión de afectos en Familia |
| QEMBAD | varchar | PK |  | SI | Embarazo Adolescente |
| QEMBR | varchar | PK |  | SI | Embarazo Riesgo (Adolescente, Patol., Obst., SPP, ... |
| QEMC | varchar | PK |  | SI | Educación (Media completa) |
| QENFCC | varchar | PK |  | SI | Enf. crónica descompensada (Cardio, Resp., Mantale... |
| QEPC | varchar | PK |  | SI | ¿Existencia de patologías crónicas? |
| QGFJHS | varchar | PK |  | SI | ¿Grupo Familiar con Jefe de hogar solo? |
| QIMSGF | varchar | PK |  | SI | Identificación de un miembro significativo para el... |
| QINGF | varchar | PK |  | SI | Ingreso Grupo Familiar |
| QJHC | varchar | PK |  | SI | Jefe de hogar cesante (Con daño econ. importante) |
| QM5ERHIRA | varchar | PK |  | SI | Menor de 5 años con Episodios Repetidos y/u Hospit... |
| QMAD | varchar | PK |  | SI | ¿Madre adolescente? |
| QMAU | varchar | PK |  | SI | Madre Ausente |
| QMNED | varchar | PK |  | SI | Mal Nutrición por exceso o déficit |
| QNEMMBC | varchar | PK |  | SI | ¿Nivel de educación materno menor que básica compl... |
| QNEMMC | varchar | PK |  | SI | ¿Nivel educacional materno menor que media complet... |
| QNEPMBC | varchar | PK |  | SI | ¿Nivel educacional paterno menor que básica comple... |
| QNEPMMC | varchar | PK |  | SI | ¿Nivel de edicación paterno menor que media comple... |
| QOTDL1 | varchar | PK |  | SI | Otra Definición Local 1: |
| QOTDL2 | varchar | PK |  | SI | Otra Definición Local 2: |
| QOTDL3 | varchar | PK |  | SI | Otra Definición Local 3: |
| QOTDL4 | varchar | PK |  | SI | Otra Definición Local 4: |
| QPACTC | varchar | PK |  | SI | Participación en actividades de la comunidad |
| QPAU | varchar | PK |  | SI | Padre Ausente |
| QPC | varchar | PK |  | SI | Poli consultantes |
| QPMCDFM | varchar | PK |  | SI | Padre/Madre con Discapacidad Física o Mental |
| QPSRAP | varchar | PK |  | SI | Postrado sin Red de Apoyo |
| QRCC | varchar | PK |  | SI | Roles de la crianza compartidos |
| QRES | varchar | PK |  | SI | Resilencia |
| QREVS | varchar | PK |  | SI | Resultado evaluación social (Sección IV - a y b) |
| QRFA | varchar | PK |  | SI | Red Familiar Activa |
| QRNPMF | varchar | PK |  | SI | RN Prematuro, Bajo peso al nacer y/o con malformac... |
| QRODTL4 | varchar | PK |  | SI | Resp. Otra Def. Local 4: |
| QROTDL1 | varchar | PK |  | SI | Resp. Otra Def. Local 1: |
| QROTDL2 | varchar | PK |  | SI | Resp. Otra Def. Local 2: |
| QROTDL3 | varchar | PK |  | SI | Resp. Otra Def. Local 3: |
| QRSA | varchar | PK |  | SI | Red Social Activa |
| QSDHF | varchar | PK |  | SI | Sentido del humor familiar |
| QTDC | varchar | PK |  | SI | Toma de decisiones compartidas |
| QTE | varchar | PK |  | SI | Trabajo Estable (Ingreso suficiente) |
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
| QVIF | varchar | PK |  | SI | VIF, Agresión a algún miembro de la Familia |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*