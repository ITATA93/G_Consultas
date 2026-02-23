# questionnaire.QTCEFORM2

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| QCI | varchar | PK |  | SI | C.I. |
| QCasoConcen | varchar | PK |  | SI | En caso de uso concentrador |
| QComuna | varchar | PK |  | SI | Comuna |
| QConclusion | varchar | PK |  | SI | De acuerdo a la evaluación es posible |
| QConclusionCon | varchar | PK |  | SI | Es posible el uso de un concentrador |
| QCondPiso | varchar | PK |  | SI | Las condiciones del piso de la habitación son adec... |
| QConsultorio | varchar | PK |  | SI | Consultorio |
| QDomic | varchar | PK |  | SI | Domicilio |
| QEnchufes | varchar | PK |  | SI | Enchufes habitación en buen estado |
| QExistEspac | varchar | PK |  | SI | Existe espacio físico suficiente para instalar equ... |
| QFechaReg | date | PK |  | SI | Fecha Registro |
| QHoraReg | time | PK |  | SI | Hora Registro |
| QLaHabit | varchar | PK |  | SI | La Habitación del paciente permite acceso expedito... |
| QNombreT | varchar | PK |  | SI | Nombre Tutor |
| QNombreprof | varchar | PK |  | SI | Nombre del Profesional de APS |
| QObserv | varchar | PK |  | SI | Observaciones |
| QPrev | varchar | PK |  | SI | Previsión |
| QRUTT | varchar | PK |  | SI | RUT Tutor |
| QRegion | varchar | PK |  | SI | Región |
| QRut | varchar | PK |  | SI | Rut |
| QSenor | varchar | PK |  | SI | Señor |
| QServicio | varchar | PK |  | SI | Servicio de Salud |
| QSumin | varchar | PK |  | SI | Suministro Eléctrico |
| QTelef | varchar | PK |  | SI | Teléfono |
| QTipoViv | varchar | PK |  | SI | Tipo de Vivienda permite la instalación de oxigeno |
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
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |
| QVivienda | varchar | PK |  | SI | Vivienda con acceso vehicular |
| QZonaU | varchar | PK |  | SI | Zona de Ubicación |
| QexisteTu | varchar | PK |  | SI | Existe un tutor adecuado |
| Qviveprimer | varchar | PK |  | SI | Vive |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*