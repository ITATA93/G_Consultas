# questionnaire.QTCEFICHAER

> Ficha ERA

**Schema:** questionnaire
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(Ficha ERA)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q38 | date |  |  | SI | F.I. Síndrome Bronquial Obstructivo Recurrente Lev... |
| Q39 | date |  |  | SI | F.E. Síndrome Bronquial Obstructivo Recurrente Lev... |
| Q40 | date |  |  | SI | F.I. Síndrome Bronquial Obstructivo Recurrente Mod... |
| Q41 | date |  |  | SI | F.E. Síndrome Bronquial Obstructivo Recurrente Mod... |
| Q42 | date |  |  | SI | F.I. Síndrome Bronquial Obstructivo Recurrente Sev... |
| Q43 | date |  |  | SI | F.E. Síndrome Bronquial Obstructivo Recurrente Sev... |
| Q44 | date |  |  | SI | F.I. Asma Bronquial Leve |
| Q45 | date |  |  | SI | F.E. Asma Bronquial Leve |
| Q46 | date |  |  | SI | F.I. Asma Bronquial Moderado |
| Q47 | date |  |  | SI | F.E. Asma Bronquial Moderado |
| Q48 | date |  |  | SI | F.I. Asma Bronquial Severo |
| Q49 | date |  |  | SI | F.E. Asma Bronquial Severo |
| Q50 | date |  |  | SI | F.I. Enfermedad Pulmonar Obstructiva Crónica A |
| Q51 | date |  |  | SI | F.E. Enfermedad Pulmonar Obstructiva Crónica A |
| Q52 | date |  |  | SI | F.I. Enfermedad Pulmonar Obstructiva Crónica B |
| Q53 | date |  |  | SI | F.E. Enfermedad Pulmonar Obstructiva Crónica B |
| Q54 | date |  |  | SI | F.I. Bronquitis Obstructiva |
| Q55 | date |  |  | SI | F.E. Bronquitis Obstructiva |
| Q56 | date |  |  | SI | F.I. Otras Iras Bajas |
| Q57 | date |  |  | SI | F.E. Otras Iras Bajas |
| Q58 | varchar |  |  | SI | M.E. Síndrome Bronquial Obstructivo Recurrente Lev... |
| Q59 | varchar |  |  | SI | M.E. Síndrome Bronquial Obstructivo Recurrente Mod... |
| Q60 | varchar |  |  | SI | M.E. Síndrome Bronquial Obstructivo Recurrente Sev... |
| Q61 | varchar |  |  | SI | M.E. Asma Bronquial Leve |
| Q62 | varchar |  |  | SI | M.E. Asma Bronquial Moderado |
| Q63 | varchar |  |  | SI | M.E. Asma Bronquial Severo |
| Q64 | varchar |  |  | SI | M.E. Enfermedad Pulmonar Obstructiva Crónica A |
| Q65 | varchar |  |  | SI | M.E. Enfermedad Pulmonar Obstructiva Crónica B |
| Q66 | varchar |  |  | SI | M.E. Bronquitis Obstructiva |
| Q67 | varchar |  |  | SI | M.E. Otras Iras Bajas |
| Q68 | varchar |  |  | SI | Si ya aplicó encuesta de calidad de vida hace un a... |
| Q69 | date |  |  | SI | FI IRA Alta  |
| Q70 | date |  |  | SI | FE IRA Alta |
| Q71 | varchar |  |  | SI | E IRA Alta |
| Q72 | date |  |  | SI | FI Influenza |
| Q73 | date |  |  | SI | FE Influenza |
| Q74 | varchar |  |  | SI | E Influenza |
| Q75 | date |  |  | SI | FI Neumonía |
| Q76 | date |  |  | SI | FE Neumonía |
| Q77 | varchar |  |  | SI | E Neumonía |
| Q78 | date |  |  | SI | FI Coqueluche |
| Q79 | date |  |  | SI | FE Coqueluche |
| Q80 | varchar |  |  | SI | E Coqueluche |
| Q81 | date |  |  | SI | FI Fibrosis Quística |
| Q82 | date |  |  | SI | FE Fibrosis Quística |
| Q83 | varchar |  |  | SI | E Fibrosis Quística |
| Q84 | date |  |  | SI | FI Displasia Broncopulmonar |
| Q85 | date |  |  | SI | FE Displasia Broncopulmonar |
| Q86 | varchar |  |  | SI | E Displasia Broncopulmonar |
| Q87 | date |  |  | SI | F.I. Otras Respiratorias Crónicas |
| Q88 | date |  |  | SI | F.E. Otras Respiratorias Crónicas |
| Q89 | varchar |  |  | SI | E Otras Respiratorias Crónicas |
| Q90 | varchar |  |  | SI | El ingreso / Re-Ingreso es por exacerbación de alg... |
| Q91 | varchar |  |  | SI | Cuáles (Selecciones según el número de la patologí... |
| Q92 | date |  |  | SI | FI Oxígeno Dependietne |
| Q93 | date |  |  | SI | FE Oxígeno Dependiente |
| Q94 | varchar |  |  | SI | E Oxígeno Dependiente |
| Q95 | date |  |  | SI | FI Asistencia Ventilatoria No Invasiva o Invasiva |
| Q96 | date |  |  | SI | FE Asistencia Ventilatoria No Invasiva o Invasiva |
| Q97 | varchar |  |  | SI | E Asistencia Ventilatoria No Invasiva o Invasiva |
| QActividad | varchar |  |  | SI | Actividad |
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
| QFechaControl | date |  |  | SI | Próximo Control (estimado) |
| QFechaReg | date |  |  | SI | Fecha Registro |
| QHoraReg | time |  |  | SI | Hora Registro |
| QNFam | numeric |  |  | SI | Número Familia |
| QOcupAnt | varchar |  |  | SI | Ocupación Anterior |
| QOcupAntObsDR | varchar |  | FK | SI | Ocupación Anterior DR |
| QOrigen | varchar |  |  | SI | Origen |
| QOrigenObsDR | varchar |  | FK | SI | Origen DR |
| QPaciente | varchar |  |  | SI | Paciente |
| QPrev | varchar |  |  | SI | Previsión |
| QProxCont | bit |  |  | SI | Próximo Control |
| QRCDA | varchar |  |  | SI | Resultado Puntaje Criterios Diagnósticos Asma |
| QRCDAObsDR | varchar |  | FK | SI | Resultado Puntaje Criterios Diagnósticos Asma DR |
| QRPCA | varchar |  |  | SI | Resultado Puntaje Control Asma |
| QRPCAObsDR | varchar |  | FK | SI | Resultado Puntaje Control Asma DR |
| QRTM6M | varchar |  |  | SI | Resultado Test Marcha 6 Min |
| QRTM6MObsDR | varchar |  | FK | SI | Resultado Test Marcha 6 Min DR |
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