# questionnaire.QTCENGB

**Schema:** questionnaire
**Columnas:** 164
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | I. IDENTIFICACIÓN DE LA INSTITUCIÓN QUE NOTIFICA |
| Q02 | numeric | PK |  | SI | N° de Caso |
| Q03 | varchar | PK |  | SI | Región |
| Q04 | varchar | PK |  | SI | Provincia |
| Q05 | varchar | PK |  | SI | Comuna |
| Q06 | varchar | PK |  | SI | Institución que Notifica |
| Q07 | varchar | PK |  | SI | Notificado Por |
| Q08 | varchar | PK |  | SI | Tipo de Sector de Institución |
| Q09 | varchar | PK |  | SI | Otro (Cuál) |
| Q10 | date | PK |  | SI | Fecha de Consulta |
| Q100 | varchar | PK |  | SI | Sensibilidad aumentada Inferior Der. |
| Q101 | varchar | PK |  | SI | Sensibilidad disminuida Superior Izq. |
| Q102 | varchar | PK |  | SI | Sensibilidad disminuida Superior Der. |
| Q103 | varchar | PK |  | SI | Sensibilidad disminuida Inferior Izq. |
| Q104 | varchar | PK |  | SI | Sensibilidad disminuida Inferior Der. |
| Q105 | varchar | PK |  | SI | Sensibilidad ausente Superior Izq. |
| Q106 | varchar | PK |  | SI | Sensibilidad ausente Superior Der. |
| Q107 | varchar | PK |  | SI | Sensibilidad ausente Inferior Izq. |
| Q108 | varchar | PK |  | SI | Sensibilidad ausente Inferior Der. |
| Q109 | varchar | PK |  | SI | Si fué hospitalizado, nombre del Hospital |
| Q11 | date | PK |  | SI | Fecha Notificación Seremi |
| Q110 | date | PK |  | SI | Fecha de Hospitalización |
| Q111 | varchar | PK |  | SI | Defunción |
| Q112 | varchar | PK |  | SI | Causa de Defunción |
| Q113 | varchar | PK |  | SI | VI. LABORATORIO |
| Q114 | date | PK |  | SI | Fecha toma de muestra |
| Q115 | date | PK |  | SI | Fecha de envío de muestra |
| Q116 | date | PK |  | SI | Fecha de recepción |
| Q118 | varchar | PK |  | SI | VII. SEGUIMIENTO A LOS 60 DÍAS |
| Q119 | date | PK |  | SI | Fecha de seguimiento |
| Q12 | date | PK |  | SI | Fecha Investigación |
| Q120 | varchar | PK |  | SI | Parálisis residual compatible con polio |
| Q121 | varchar | PK |  | SI | Atrofia |
| Q125 | varchar | PK |  | SI | a) Pródomos |
| Q128 | varchar | PK |  | SI | b) Parálisis |
| Q129 | varchar | PK |  | SI | c) Signos |
| Q13 | date | PK |  | SI | Fecha Notificación MINSAL |
| Q130 | varchar | PK |  | SI | d) Progresión |
| Q131 | varchar | PK |  | SI | Localización Superior |
| Q132 | varchar | PK |  | SI | Localización Inferior |
| Q14 | varchar | PK |  | SI | Detectado por |
| Q15 | varchar | PK |  | SI | Búsqueda Institucional |
| Q16 | varchar | PK |  | SI | Búsqueda Institucional |
| Q17 | varchar | PK |  | SI | II. INFORMACIÓN DEL PACIENTE |
| Q18 | varchar | PK |  | SI | Nacionalidad |
| Q19 | numeric | PK |  | SI | Teléfono |
| Q20 | varchar | PK |  | SI | Comuna |
| Q21 | varchar | PK |  | SI | Región |
| Q22 | varchar | PK |  | SI | Tipo de Localidad |
| Q23 | varchar | PK |  | SI | Ocupación del Paciente |
| Q24 | varchar | PK |  | SI | III. HISTORIA VACUNAL |
| Q25 | varchar | PK |  | SI | Tipo De Vacuna Polio |
| Q26 | numeric | PK |  | SI | N° Dosis |
| Q27 | date | PK |  | SI | Fecha Última Dosis |
| Q28 | varchar | PK |  | SI | Fuente de Información sobre la Vacuna |
| Q29 | varchar | PK |  | SI | Antecedente de Vacuna influenza |
| Q30 | varchar | PK |  | SI | Cual |
| Q31 | varchar | PK |  | SI | Marca de Vacuna |
| Q32 | varchar | PK |  | SI | Lote |
| Q33 | date | PK |  | SI | Fecha de Administración |
| Q34 | varchar | PK |  | SI | Lugar donde fué administrada o adquirida |
| Q35 | varchar | PK |  | SI | IV. ANTECEDENTES DE VIAJES |
| Q36 | varchar | PK |  | SI | Durante los últimos 2 meses, ha viajado |
| Q37 | varchar | PK |  | SI | País |
| Q38 | varchar | PK |  | SI | Ciudad |
| Q39 | date | PK |  | SI | Fecha de Entrada |
| Q40 | date | PK |  | SI | Fecha de Salida |
| Q41 | varchar | PK |  | SI | V. DATOS CLÍNICOS |
| Q42 | varchar | PK |  | SI | Pródomos |
| Q43 | varchar | PK |  | SI | Fiebre |
| Q44 | varchar | PK |  | SI | Cuadro Respiratorio |
| Q45 | varchar | PK |  | SI | Cuadro Gastrointestinal |
| Q46 | date | PK |  | SI | Fecha de Inicio de este cuadro |
| Q47 | varchar | PK |  | SI | Ha presentado en otra ocasión SGB, PFA o Neuropatí... |
| Q48 | varchar | PK |  | SI | Cual |
| Q49 | varchar | PK |  | SI | Fecha o Año |
| Q50 | varchar | PK |  | SI | Parálisis |
| Q51 | date | PK |  | SI | Fecha inicio |
| Q52 | varchar | PK |  | SI | Fiebre al Inicio de parálisis |
| Q53 | varchar | PK |  | SI | Compromiso pares craneales |
| Q54 | varchar | PK |  | SI | Compromiso Respiratorio |
| Q55 | varchar | PK |  | SI | Signos |
| Q56 | varchar | PK |  | SI | Dolores Musculares |
| Q57 | varchar | PK |  | SI | Signos Meníngeos |
| Q58 | varchar | PK |  | SI | Progresión |
| Q59 | varchar | PK |  | SI | Dirección |
| Q60 | varchar | PK |  | SI | Días hasta la instalación de parálisis completa |
| Q61 | varchar | PK |  | SI | Parálisis Superior Izq. |
| Q62 | varchar | PK |  | SI | Parálisis Superior Der. |
| Q63 | varchar | PK |  | SI | Parálisis Inferior Izq.  |
| Q64 | varchar | PK |  | SI | Parálisis Inferior Der.  |
| Q65 | varchar | PK |  | SI | Fláccida Superior Izq. |
| Q66 | varchar | PK |  | SI | Fláccida Superior Der. |
| Q67 | varchar | PK |  | SI | Fláccida Inferior Izq. |
| Q68 | varchar | PK |  | SI | Fláccida Inferior Der. |
| Q69 | varchar | PK |  | SI | Distribución proximal Superior Izq. |
| Q70 | varchar | PK |  | SI | Distribución proximal Superior Der. |
| Q71 | varchar | PK |  | SI | Distribución proximal Inferior Izq. |
| Q72 | varchar | PK |  | SI | Distribución proximal Inferior Der. |
| Q73 | varchar | PK |  | SI | Distribución distal Superior Izq |
| Q74 | varchar | PK |  | SI | Distribución distal Superior Der. |
| Q75 | varchar | PK |  | SI | Distribución distal Inferior Izq. |
| Q76 | varchar | PK |  | SI | Distribución distal Inferior Der. |
| Q77 | varchar | PK |  | SI | Reflejos osteotendíneos normales Superior Izq. |
| Q78 | varchar | PK |  | SI | Reflejos osteotendíneos normales Superior Der. |
| Q79 | varchar | PK |  | SI | Reflejos osteotendíneos normales Inferior Izq. |
| Q80 | varchar | PK |  | SI | Reflejos osteotendíneos normales Inferior Der. |
| Q81 | varchar | PK |  | SI | Reflejos osteotendíneos aumentado Superior Izq. |
| Q82 | varchar | PK |  | SI | Reflejos osteotendíneos aumentado Superior Der. |
| Q83 | varchar | PK |  | SI | Reflejos osteotendíneos aumentado Inferior Izq. |
| Q84 | varchar | PK |  | SI | Reflejos osteotendíneos aumentado Inferior Der. |
| Q85 | varchar | PK |  | SI | Reflejos osteotendíneos disminuidos Superior Izq. |
| Q86 | varchar | PK |  | SI | Reflejos osteotendíneos disminuidos Superior Der. |
| Q87 | varchar | PK |  | SI | Reflejos osteotendíneos disminuidos Inferior Izq. |
| Q88 | varchar | PK |  | SI | Reflejos osteotendíneos disminuidos Inferior Der. |
| Q89 | varchar | PK |  | SI | Reflejos osteotendíneos ausentes Superior Izq. |
| Q90 | varchar | PK |  | SI | Reflejos osteotendíneos ausentes Superior Der. |
| Q91 | varchar | PK |  | SI | Reflejos osteotendíneos ausentes Inferior Izq. |
| Q92 | varchar | PK |  | SI | Reflejos osteotendíneos ausentes Inferior Der. |
| Q93 | varchar | PK |  | SI | Sensibilidad normal Superior Izq. |
| Q94 | varchar | PK |  | SI | Sensibilidad normal Superior Der. |
| Q95 | varchar | PK |  | SI | Sensibilidad normal Inferior Izq. |
| Q96 | varchar | PK |  | SI | Sensibilidad normal Inferior Der. |
| Q97 | varchar | PK |  | SI | Sensibilidad aumentada Superior Izq. |
| Q98 | varchar | PK |  | SI | Sensibilidad aumentada Superior Der. |
| Q99 | varchar | PK |  | SI | Sensibilidad aumentada Inferior Izq. |
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