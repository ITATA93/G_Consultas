# SQLUser.LBC_SpecimenAnatomicalSite

**Schema:** SQLUser
**Columnas:** 152
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSPAS_ParRef | bigint | PK |  | NO | Parent Specimen DR |
| ChildQExaDR | - |  |  | SI | Child Reference: Exámenes |
| LBCSPAS_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site DR |
| LBCSPAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPAS_RowID | varchar |  |  | NO | - |
| Q38 | - |  |  | SI | F.I. Síndrome Bronquial Obstructivo Recurrente Lev... |
| Q39 | - |  |  | SI | F.E. Síndrome Bronquial Obstructivo Recurrente Lev... |
| Q40 | - |  |  | SI | F.I. Síndrome Bronquial Obstructivo Recurrente Mod... |
| Q41 | - |  |  | SI | F.E. Síndrome Bronquial Obstructivo Recurrente Mod... |
| Q42 | - |  |  | SI | F.I. Síndrome Bronquial Obstructivo Recurrente Sev... |
| Q43 | - |  |  | SI | F.E. Síndrome Bronquial Obstructivo Recurrente Sev... |
| Q44 | - |  |  | SI | F.I. Asma Bronquial Leve |
| Q45 | - |  |  | SI | F.E. Asma Bronquial Leve |
| Q46 | - |  |  | SI | F.I. Asma Bronquial Moderado |
| Q47 | - |  |  | SI | F.E. Asma Bronquial Moderado |
| Q48 | - |  |  | SI | F.I. Asma Bronquial Severo |
| Q49 | - |  |  | SI | F.E. Asma Bronquial Severo |
| Q50 | - |  |  | SI | F.I. Enfermedad Pulmonar Obstructiva Crónica A |
| Q51 | - |  |  | SI | F.E. Enfermedad Pulmonar Obstructiva Crónica A |
| Q52 | - |  |  | SI | F.I. Enfermedad Pulmonar Obstructiva Crónica B |
| Q53 | - |  |  | SI | F.E. Enfermedad Pulmonar Obstructiva Crónica B |
| Q54 | - |  |  | SI | F.I. Bronquitis Obstructiva |
| Q55 | - |  |  | SI | F.E. Bronquitis Obstructiva |
| Q56 | - |  |  | SI | F.I. Otras Iras Bajas |
| Q57 | - |  |  | SI | F.E. Otras Iras Bajas |
| Q58 | - |  |  | SI | M.E. Síndrome Bronquial Obstructivo Recurrente Lev... |
| Q59 | - |  |  | SI | M.E. Síndrome Bronquial Obstructivo Recurrente Mod... |
| Q60 | - |  |  | SI | M.E. Síndrome Bronquial Obstructivo Recurrente Sev... |
| Q61 | - |  |  | SI | M.E. Asma Bronquial Leve |
| Q62 | - |  |  | SI | M.E. Asma Bronquial Moderado |
| Q63 | - |  |  | SI | M.E. Asma Bronquial Severo |
| Q64 | - |  |  | SI | M.E. Enfermedad Pulmonar Obstructiva Crónica A |
| Q65 | - |  |  | SI | M.E. Enfermedad Pulmonar Obstructiva Crónica B |
| Q66 | - |  |  | SI | M.E. Bronquitis Obstructiva |
| Q67 | - |  |  | SI | M.E. Otras Iras Bajas |
| Q68 | - |  |  | SI | Si ya aplicó encuesta de calidad de vida hace un a... |
| Q69 | - |  |  | SI | FI IRA Alta |
| Q70 | - |  |  | SI | FE IRA Alta |
| Q71 | - |  |  | SI | E IRA Alta |
| Q72 | - |  |  | SI | FI Influenza |
| Q73 | - |  |  | SI | FE Influenza |
| Q74 | - |  |  | SI | E Influenza |
| Q75 | - |  |  | SI | FI Neumonía |
| Q76 | - |  |  | SI | FE Neumonía |
| Q77 | - |  |  | SI | E Neumonía |
| Q78 | - |  |  | SI | FI Coqueluche |
| Q79 | - |  |  | SI | FE Coqueluche |
| Q80 | - |  |  | SI | E Coqueluche |
| Q81 | - |  |  | SI | FI Fibrosis Quística |
| Q82 | - |  |  | SI | FE Fibrosis Quística |
| Q83 | - |  |  | SI | E Fibrosis Quística |
| Q84 | - |  |  | SI | FI Displasia Broncopulmonar |
| Q85 | - |  |  | SI | FE Displasia Broncopulmonar |
| Q86 | - |  |  | SI | E Displasia Broncopulmonar |
| Q87 | - |  |  | SI | F.I. Otras Respiratorias Crónicas |
| Q88 | - |  |  | SI | F.E. Otras Respiratorias Crónicas |
| Q89 | - |  |  | SI | E Otras Respiratorias Crónicas |
| Q90 | - |  |  | SI | El ingreso / Re-Ingreso es por exacerbación de alg... |
| Q91 | - |  |  | SI | Cuáles (Selecciones según el número de la patologí... |
| Q92 | - |  |  | SI | FI Oxígeno Dependietne |
| Q93 | - |  |  | SI | FE Oxígeno Dependiente |
| Q94 | - |  |  | SI | E Oxígeno Dependiente |
| Q95 | - |  |  | SI | FI Asistencia Ventilatoria No Invasiva o Invasiva |
| Q96 | - |  |  | SI | FE Asistencia Ventilatoria No Invasiva o Invasiva |
| Q97 | - |  |  | SI | E Asistencia Ventilatoria No Invasiva o Invasiva |
| QActividad | - |  |  | SI | Actividad |
| QComuna | - |  |  | SI | Comuna |
| QConsultorio | - |  |  | SI | Consultorio |
| QDerivadar | - |  |  | SI | Derivar a consejería |
| QDestino | - |  |  | SI | Destino |
| QDestinoObsDR | - |  |  | SI | Destino DR |
| QDomic | - |  |  | SI | Domicilio |
| QECVC | - |  |  | SI | Encuesta Calidad de Vida de Control |
| QECVI | - |  |  | SI | Encuesta Calidad de Vida al Ingreso |
| QESU | - |  |  | SI | Encuenta Satisfacción Usuaria |
| QEdu | - |  |  | SI | Educación en Box (Técnica inhalatoria, manejo ambi... |
| QExamen | - |  |  | SI | Exámen |
| QFechaControl | - |  |  | SI | Próximo Control (estimado) |
| QFechaReg | - |  |  | SI | Fecha Registro |
| QHoraReg | - |  |  | SI | Hora Registro |
| QNFam | - |  |  | SI | Número Familia |
| QOcupAnt | - |  |  | SI | Ocupación Anterior |
| QOcupAntObsDR | - |  |  | SI | Ocupación Anterior DR |
| QOrigen | - |  |  | SI | Origen |
| QOrigenObsDR | - |  |  | SI | Origen DR |
| QPaciente | - |  |  | SI | Paciente |
| QPrev | - |  |  | SI | Previsión |
| QProxCont | - |  |  | SI | Próximo Control |
| QRCDA | - |  |  | SI | Resultado Puntaje Criterios Diagnósticos Asma |
| QRCDAObsDR | - |  |  | SI | Resultado Puntaje Criterios Diagnósticos Asma DR |
| QRPCA | - |  |  | SI | Resultado Puntaje Control Asma |
| QRPCAObsDR | - |  |  | SI | Resultado Puntaje Control Asma DR |
| QRTM6M | - |  |  | SI | Resultado Test Marcha 6 Min |
| QRTM6MObsDR | - |  |  | SI | Resultado Test Marcha 6 Min DR |
| QRegion | - |  |  | SI | Región |
| QRiesgoLab | - |  |  | SI | Riesgo Laboral |
| QRiesgoLabObsDR | - |  |  | SI | Riesgo Laboral DR |
| QRut | - |  |  | SI | Rut |
| QServicio | - |  |  | SI | Servicio de Salud |
| QTab1 | - |  |  | SI | Años Fumando |
| QTab1ObsDR | - |  |  | SI | Años Fumando DR |
| QTab2 | - |  |  | SI | Cigarros al Día |
| QTab2ObsDR | - |  |  | SI | Cigarros al Día DR |
| QTab3 | - |  |  | SI | Paquetes al Año |
| QTab3ObsDR | - |  |  | SI | Paquetes al Año DR |
| QTelef | - |  |  | SI | Teléfono |
| QTest6m | - |  |  | SI | A Test de 6 minutos |
| QTipoProf | - |  |  | SI | Tipo Profesional |
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
| QViveCon | - |  |  | SI | Vive con |
| QViveConObsDR | - |  |  | SI | Vive con  DR |
| Qvacun | - |  |  | SI | A Vacunación |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*