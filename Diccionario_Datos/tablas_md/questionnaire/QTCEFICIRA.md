# questionnaire.QTCEFICIRA

> Ficha IRA

**Schema:** questionnaire
**Columnas:** 140
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(Ficha IRA)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q30 | varchar |  |  | SI | Escolaridad |
| Q31 | varchar |  |  | SI | Resultado Riesgo Morir de Bronconeumonía |
| Q35 | date |  |  | SI | FI Síndrome Bronquial Obstructivo Recurrente Leve |
| Q36 | date |  |  | SI | FE Síndrome Bronquial Obstructivo Recurrente Leve |
| Q37 | date |  |  | SI | FI Síndrome Bronquial Obstructivo Recurrente Moder... |
| Q38 | date |  |  | SI | FE Síndrome Bronquial Obstructivo Recurrente Moder... |
| Q39 | date |  |  | SI | FI Síndrome Bronquial Obstructivo Recurrente Sever... |
| Q40 | date |  |  | SI | FE Síndrome Bronquial Obstructivo Recurrente Sever... |
| Q41 | date |  |  | SI | FI Asma Bronquial Leve |
| Q42 | date |  |  | SI | FE Asma Bronquial Leve |
| Q43 | date |  |  | SI | FI Asma Bronquial Moderado |
| Q44 | date |  |  | SI | FE Asma Bronquial Moderado |
| Q45 | date |  |  | SI | FI Asma Bronquial Severo |
| Q46 | date |  |  | SI | FE Asma Bronquial Severo |
| Q47 | date |  |  | SI | FI Enfermedad Pulmonar Obstructiva Crónica A |
| Q48 | date |  |  | SI | FE Enfermedad Pulmonar Obstructiva Crónica A |
| Q49 | date |  |  | SI | FI Enfermedad Pulmonar Obstructiva Crónica B |
| Q50 | date |  |  | SI | FE Enfermedad Pulmonar Obstructiva Crónica B |
| Q51 | date |  |  | SI | FI Bronquitis Obstructiva |
| Q52 | date |  |  | SI | FE Bronquitis Obstructiva |
| Q53 | date |  |  | SI | FE Otras Iras Bajas |
| Q54 | date |  |  | SI | FI Otras Iras Bajas |
| Q55 | varchar |  |  | SI | E Síndrome Bronquial Obstructivo Recurrente Leve |
| Q56 | varchar |  |  | SI | E Síndrome Bronquial Obstructivo Recurrente Modera... |
| Q57 | varchar |  |  | SI | E Síndrome Bronquial Obstructivo Recurrente Severo |
| Q58 | varchar |  |  | SI | E Asma Bronquial Leve |
| Q59 | varchar |  |  | SI | E Asma Bronquial Moderado |
| Q60 | varchar |  |  | SI | E Asma Bronquial Severo |
| Q61 | varchar |  |  | SI | E Enfermedad Pulmonar Obstructiva Crónica A |
| Q62 | varchar |  |  | SI | E Enfermedad Pulmonar Obstructiva Crónica B |
| Q63 | varchar |  |  | SI | E Bronquitis Obstructiva |
| Q64 | varchar |  |  | SI | E Otras Iras Bajas |
| Q65 | varchar |  |  | SI | Si ya aplicó encuesta de calidad de vida hace un a... |
| Q66 | date |  |  | SI | FI IRA Alta  |
| Q67 | date |  |  | SI | FE IRA Alta |
| Q68 | varchar |  |  | SI | E IRA Alta |
| Q69 | date |  |  | SI | FI Influenza |
| Q70 | date |  |  | SI | FE Influenza |
| Q71 | varchar |  |  | SI | E Influenza |
| Q72 | date |  |  | SI | FI Neumonía |
| Q73 | date |  |  | SI | FE Neumonía |
| Q74 | varchar |  |  | SI | E Neumonía |
| Q75 | date |  |  | SI | FI Coqueluche |
| Q76 | date |  |  | SI | FE Coqueluche |
| Q77 | varchar |  |  | SI | E Coqueluche |
| Q78 | date |  |  | SI | FI Fibrosis Quística |
| Q79 | date |  |  | SI | FE Fibrosis Quística |
| Q80 | varchar |  |  | SI | E Fibrosis Quísitca |
| Q81 | date |  |  | SI | FI Displasia Broncopulmonar |
| Q82 | date |  |  | SI | FE Displasia Broncopulmonar |
| Q83 | varchar |  |  | SI | E Displasia Broncopulmonar |
| Q84 | date |  |  | SI | FI Otras Respiratorias Crónicas |
| Q85 | date |  |  | SI | FE Otras Respiratorias Crónicas |
| Q86 | varchar |  |  | SI | E Otras Respiratorias Crónicas |
| Q87 | varchar |  |  | SI | ¿El ingreso / Re-Ingreso es por exacerbación de al... |
| Q88 | varchar |  |  | SI | Cuáles (Selecciones según el número de la patologí... |
| Q89 | date |  |  | SI | FI Oxigeno Dependiente |
| Q90 | date |  |  | SI | FE Oxígeno Dependente |
| Q91 | varchar |  |  | SI | E Oxígeno Dependiente |
| Q92 | date |  |  | SI | FI Asistencia Ventilatoria No Invasiva o Invasiva |
| Q93 | date |  |  | SI | FE Asistencia Ventilatoria No Invasiva o Invasiva |
| Q94 | varchar |  |  | SI | E Asistencia Ventilatoria No Invasiva o Invasiva |
| QComuna | varchar |  |  | SI | Comuna |
| QConsultorio | varchar |  |  | SI | Consultorio |
| QDerivadar | bit |  |  | SI | Derivar a consejería |
| QDestino | varchar |  |  | SI | Destino |
| QDestinoObsDR | varchar |  | FK | SI | Destino DR |
| QDomic | varchar |  |  | SI | Domicilio |
| QECVC | varchar |  |  | SI | Encuesta Calidad de Vida de Control |
| QECVI | varchar |  |  | SI | Encuesta Calidad de Vida al Ingreso |
| QESU | varchar |  |  | SI | Encuenta Satisfacción Usuaria |
| QEdu | varchar |  |  | SI | Educación en Box (Técnica inhalatoria, manejo ambi... |
| QExamen | varchar |  |  | SI | Exámen |
| QFechaControl | date |  |  | SI | Fecha próximo Control |
| QFechaReg | date |  |  | SI | Fecha Registro |
| QHoraReg | time |  |  | SI | Hora Registro |
| QNFam | numeric |  |  | SI | Número Familia |
| QOrigen | varchar |  |  | SI | Origen |
| QOrigenObsDR | varchar |  | FK | SI | Origen DR |
| QPaciente | varchar |  |  | SI | Paciente |
| QPrev | varchar |  |  | SI | Previsión |
| QProxCont | bit |  |  | SI | Próximo Control |
| QRegion | varchar |  |  | SI | Región |
| QRiesgoLab | varchar |  |  | SI | Riesgo Laboral |
| QRiesgoLabObsDR | varchar |  | FK | SI | Riesgo Laboral DR |
| QRut | varchar |  |  | SI | Rut |
| QServicio | varchar |  |  | SI | Servicio de Salud |
| QTab1 | varchar |  |  | SI | Años Fumando |
| QTab1ObsDR | varchar |  | FK | SI | Años Fumando DR |
| QTab2 | varchar |  |  | SI | Cigarros al Día |
| QTab2ObsDR | varchar |  | FK | SI | Cigarros al Día DR |
| QTab3 | varchar |  |  | SI | Paquetes al Año |
| QTab3ObsDR | varchar |  | FK | SI | Paquetes al Año DR |
| QTelef | varchar |  |  | SI | Teléfono |
| QTest6m | bit |  |  | SI | A Test de 6 minutos |
| QTipoProf | varchar |  |  | SI | Tipo Profesional |
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
| QViveCon | varchar |  |  | SI | Vive con  |
| QViveConObsDR | varchar |  | FK | SI | Vive con  DR |
| Qvacun | bit |  |  | SI | A Vacunación |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*