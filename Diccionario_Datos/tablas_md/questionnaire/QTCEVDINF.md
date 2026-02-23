# questionnaire.QTCEVDINF

> Visita Domiciliaria Integral

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Visita Domiciliaria Integral

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Integrantes del equipo de visita |
| Q02 | varchar |  |  | SI | Motivo de la Visita |
| Q03 | varchar |  |  | SI | Antecedentes de la Familia |
| Q04 | numeric |  |  | SI | N° de personas que viven en la casa |
| Q05 | numeric |  |  | SI | N° Adultos |
| Q06 | numeric |  |  | SI | N° de Niños menores de 6 años |
| Q07 | varchar |  |  | SI | Jefe de Hogar |
| Q08 | varchar |  |  | SI | Otros |
| Q09 | numeric |  |  | SI | N° Familias que viven el en domicilio |
| Q61 | varchar |  |  | SI | Indicación de Nutrición Enteral Domiciliaria (NED) |
| Q62 | varchar |  |  | SI | Especialidad |
| QAD1 | varchar |  |  | SI | Se observan juguetes adecuados para la edad del ni... |
| QAD2 | varchar |  |  | SI | Se observa la existencia de libros, cuentos infant... |
| QAD3 | varchar |  |  | SI | Se observa en general un desorden, caos, en las co... |
| QAD4 | varchar |  |  | SI | El niño duerme solo en su cama o cuna |
| QAD5 | varchar |  |  | SI | Existe peligro de accidente en el interior del hog... |
| QAD6 | varchar |  |  | SI | Existe un lugar donde el niño/a pueda jugar en la ... |
| QFP1 | varchar |  |  | SI | Red familiar activa |
| QFP10 | varchar |  |  | SI | Identificación de un miembro significativo para el... |
| QFP11 | varchar |  |  | SI | Actividades familiares compartidas |
| QFP12 | varchar |  |  | SI | Otras: |
| QFP12a | varchar |  |  | SI | Otras: Texto |
| QFP2 | varchar |  |  | SI | Red social activa |
| QFP3 | varchar |  |  | SI | Trabajo Estable (ingreso suficiente) |
| QFP4 | varchar |  |  | SI | Educación media completa |
| QFP5 | varchar |  |  | SI | Buena comunicación familiar |
| QFP6 | varchar |  |  | SI | Expresión de afectos de familia |
| QFP7 | varchar |  |  | SI | Estructura familiar democrática |
| QFP8 | varchar |  |  | SI | Controles al día |
| QFP9 | varchar |  |  | SI | Sentido del humor en la familia |
| QIB1 | varchar |  |  | SI | Existencia de junta de vecinos |
| QIB10 | varchar |  |  | SI | Percepción de inseguridad (delicuencia, drogas, pr... |
| QIB11 | varchar |  |  | SI | Otros |
| QIB2 | varchar |  |  | SI | Existencia de otras organizaciones comunitarias |
| QIB3 | varchar |  |  | SI | Sistema de locomoción frecuente y de fácil acceso |
| QIB4 | varchar |  |  | SI | Sector dispone de areas verdes y recreativas (plaz... |
| QIB5 | varchar |  |  | SI | El barrio cuenta con escuelas |
| QIB6 | varchar |  |  | SI | El barrio cuenta con salas cunas y jardines infant... |
| QIB7 | varchar |  |  | SI | El barrio cuenta con centro de salud |
| QIB8 | varchar |  |  | SI | El acceso a centros de salud es adecuado |
| QIB9 | varchar |  |  | SI | El acceso a otros servicios comunitarios es adecua... |
| QIE01 | varchar |  |  | SI | Hogar libre del humo de tabaco |
| QIE02 | varchar |  |  | SI | Por Muerte de Neumonía en Domicilio |
| QIE03 | varchar |  |  | SI | Programa de Oxigenoterapia Ambulatoria AVNI/AVNIA |
| QIE04 | varchar |  |  | SI | Otras Visitas |
| QIE05 | varchar |  |  | SI | Patologías Respiratorias Crónicas Severas o no Con... |
| QIF1 | varchar |  |  | SI | Vivienda de construcción sólida |
| QIF10 | varchar |  |  | SI | Contaminación intradomiciliaria (humo tabaco, mala... |
| QIF11 | varchar |  |  | SI | Otros |
| QIF2 | varchar |  |  | SI | Vivienda con saneamiento básico completo (agua pot... |
| QIF3 | varchar |  |  | SI | Condiciones peligrosas o de riesgo de accidentes f... |
| QIF4 | varchar |  |  | SI | Dispone de espacio seguro (patio) para juego de ni... |
| QIF5 | varchar |  |  | SI | Conexión telefónica, televisores, internet |
| QIF6 | varchar |  |  | SI | Condiciones de hacinamiento |
| QIF7 | varchar |  |  | SI | Buenas condiciones de higiene en el hogar |
| QIF8 | varchar |  |  | SI | Presencia de animales domésticos mal cuidados |
| QIF9 | varchar |  |  | SI | Condiciones de aislamiento geográfico o del hogar |
| QIR | varchar |  |  | SI | Integrante de la Familia que se encuentre en Progr... |
| QOV | varchar |  |  | SI | Otro tipo de Visita Integral |
| QTV59 | varchar |  |  | SI | Tipo de Visita |
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