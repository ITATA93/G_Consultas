# SQLUser.MHC_DetTypeTaskType

**Schema:** SQLUser
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TASKT_ParRef | bigint | PK |  | NO | MHC_DetentionType Parent Reference |
| ChildQRRDR | - |  |  | SI | Child Reference: Motivo / Diagnóstico / Plan de In... |
| Q01 | - |  |  | SI | Integrantes del equipo de visita |
| Q02 | - |  |  | SI | Motivo de la Visita |
| Q03 | - |  |  | SI | Antecedentes de la Familia |
| Q04 | - |  |  | SI | N° de personas que viven en la casa |
| Q05 | - |  |  | SI | N° Adultos |
| Q06 | - |  |  | SI | N° de Niños menores de 6 años |
| Q07 | - |  |  | SI | Jefe de Hogar |
| Q08 | - |  |  | SI | Otros |
| Q09 | - |  |  | SI | N° Familias que viven el en domicilio |
| Q61 | - |  |  | SI | Indicación de Nutrición Enteral Domiciliaria (NED) |
| Q62 | - |  |  | SI | Especialidad |
| QAD1 | - |  |  | SI | Se observan juguetes adecuados para la edad del ni... |
| QAD2 | - |  |  | SI | Se observa la existencia de libros, cuentos infant... |
| QAD3 | - |  |  | SI | Se observa en general un desorden, caos, en las co... |
| QAD4 | - |  |  | SI | El niño duerme solo en su cama o cuna |
| QAD5 | - |  |  | SI | Existe peligro de accidente en el interior del hog... |
| QAD6 | - |  |  | SI | Existe un lugar donde el niño/a pueda jugar en la ... |
| QFP1 | - |  |  | SI | Red familiar activa |
| QFP10 | - |  |  | SI | Identificación de un miembro significativo para el... |
| QFP11 | - |  |  | SI | Actividades familiares compartidas |
| QFP12 | - |  |  | SI | Otras: |
| QFP12a | - |  |  | SI | Otras: Texto |
| QFP2 | - |  |  | SI | Red social activa |
| QFP3 | - |  |  | SI | Trabajo Estable (ingreso suficiente) |
| QFP4 | - |  |  | SI | Educación media completa |
| QFP5 | - |  |  | SI | Buena comunicación familiar |
| QFP6 | - |  |  | SI | Expresión de afectos de familia |
| QFP7 | - |  |  | SI | Estructura familiar democrática |
| QFP8 | - |  |  | SI | Controles al día |
| QFP9 | - |  |  | SI | Sentido del humor en la familia |
| QIB1 | - |  |  | SI | Existencia de junta de vecinos |
| QIB10 | - |  |  | SI | Percepción de inseguridad (delicuencia, drogas, pr... |
| QIB11 | - |  |  | SI | Otros |
| QIB2 | - |  |  | SI | Existencia de otras organizaciones comunitarias |
| QIB3 | - |  |  | SI | Sistema de locomoción frecuente y de fácil acceso |
| QIB4 | - |  |  | SI | Sector dispone de areas verdes y recreativas (plaz... |
| QIB5 | - |  |  | SI | El barrio cuenta con escuelas |
| QIB6 | - |  |  | SI | El barrio cuenta con salas cunas y jardines infant... |
| QIB7 | - |  |  | SI | El barrio cuenta con centro de salud |
| QIB8 | - |  |  | SI | El acceso a centros de salud es adecuado |
| QIB9 | - |  |  | SI | El acceso a otros servicios comunitarios es adecua... |
| QIE01 | - |  |  | SI | Hogar libre del humo de tabaco |
| QIE02 | - |  |  | SI | Por Muerte de Neumonía en Domicilio |
| QIE03 | - |  |  | SI | Programa de Oxigenoterapia Ambulatoria AVNI/AVNIA |
| QIE04 | - |  |  | SI | Otras Visitas |
| QIE05 | - |  |  | SI | Patologías Respiratorias Crónicas Severas o no Con... |
| QIF1 | - |  |  | SI | Vivienda de construcción sólida |
| QIF10 | - |  |  | SI | Contaminación intradomiciliaria (humo tabaco, mala... |
| QIF11 | - |  |  | SI | Otros |
| QIF2 | - |  |  | SI | Vivienda con saneamiento básico completo (agua pot... |
| QIF3 | - |  |  | SI | Condiciones peligrosas o de riesgo de accidentes f... |
| QIF4 | - |  |  | SI | Dispone de espacio seguro (patio) para juego de ni... |
| QIF5 | - |  |  | SI | Conexión telefónica, televisores, internet |
| QIF6 | - |  |  | SI | Condiciones de hacinamiento |
| QIF7 | - |  |  | SI | Buenas condiciones de higiene en el hogar |
| QIF8 | - |  |  | SI | Presencia de animales domésticos mal cuidados |
| QIF9 | - |  |  | SI | Condiciones de aislamiento geográfico o del hogar |
| QIR | - |  |  | SI | Integrante de la Familia que se encuentre en Progr... |
| QOV | - |  |  | SI | Otro tipo de Visita Integral |
| QTV59 | - |  |  | SI | Tipo de Visita |
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
| TASKT_Childsub | double |  |  | NO | Childsub |
| TASKT_CreatedDate | date |  |  | SI | Created Date |
| TASKT_CreatedTime | time |  |  | SI | Created Time |
| TASKT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TASKT_RowId | varchar |  |  | NO | - |
| TASKT_TaskType_DR | bigint |  | FK | SI | Des Ref MHCTaskType |
| TASKT_UpdatedDate | date |  |  | SI | Updated Date |
| TASKT_UpdatedTime | time |  |  | SI | Updated Time |
| TASKT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*