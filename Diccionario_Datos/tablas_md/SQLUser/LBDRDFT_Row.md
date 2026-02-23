# SQLUser.LBDRDFT_Row

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRDFTR_ParRef | bigint | PK |  | NO | The DFT containing this row |
| ChildQDIAG56DR | - |  |  | SI | Child Reference: DIAGNÓSTICOS Y CÓDIGOS CIE-10 |
| LBDRDFTR_RowID | varchar |  |  | NO | - |
| LBDRDFTR_RowNo | integer |  |  | SI | The row number within the table (needed because re... |
| Q01 | - |  |  | SI | Seremi Región |
| Q02 | - |  |  | SI | Servicio Salud |
| Q03 | - |  |  | SI | Oficina Provincial |
| Q04 | - |  |  | SI | Establecimiento |
| Q05 | - |  |  | SI | Fecha Notificación |
| Q06 | - |  |  | SI | Fecha Validación SEREMI |
| Q07 | - |  |  | SI | Médico Tratante |
| Q08 | - |  |  | SI | Persona que Notifica |
| Q09 | - |  |  | SI | Teléfono |
| QCF49 | - |  |  | SI | CLASIFICACIÓN FINAL |
| QCF50 | - |  |  | SI | Confirmado o Descartado por |
| QCF51 | - |  |  | SI | Por Laboratorio |
| QIC10 | - |  |  | SI | Embarazo |
| QIC11 | - |  |  | SI | Semana de Gestación |
| QIC12 | - |  |  | SI | Ocupación |
| QIC14 | - |  |  | SI | Pertenencia declarada a algún prueblo originario |
| QIC15 | - |  |  | SI | Nacionalidad |
| QIEP39 | - |  |  | SI | Fecha Tratamiento de Contactos |
| QIEP45 | - |  |  | SI | Corresponde |
| QIEP46 | - |  |  | SI | Si corresponde, Institución donde se realizó el Bl... |
| QINFC16 | - |  |  | SI | N° de Historia Clínica |
| QINFC17 | - |  |  | SI | Fecha Primeros Síntomas |
| QINFC18 | - |  |  | SI | Fecha Primera Consulta |
| QINFC19 | - |  |  | SI | Fecha Hospitalización |
| QINFC20 | - |  |  | SI | Est. Hospitalización |
| QINFC21 | - |  |  | SI | Establecimiento Derivación |
| QINFC22 | - |  |  | SI | Diagnóstico de Ingreso |
| QINFC23 | - |  |  | SI | Caso |
| QINFC24 | - |  |  | SI | Nombre Caso Primario |
| QINFC27 | - |  |  | SI | Fallecido |
| QINFC28 | - |  |  | SI | Fecha Fallecimiento |
| QINFC29 | - |  |  | SI | Cuál |
| QINFL30 | - |  |  | SI | Fecha Toma de Muestra |
| QINFL31 | - |  |  | SI | LATEX Resultado |
| QINFL32 | - |  |  | SI | GRAM Resultado |
| QINFL33 | - |  |  | SI | CULTIVO LCR Resultado |
| QINFL34 | - |  |  | SI | HEMOCULTIVO Resultado |
| QINFL35 | - |  |  | SI | Otro Resultado |
| QINFL36 | - |  |  | SI | Fecha de Envío al ISP |
| QINFL37 | - |  |  | SI | Resultado ISP |
| QINFL38 | - |  |  | SI | Resultado Exámenes |
| QLOC51 | - |  |  | SI | Localización (Aplica en Enf. Meningocóccica o Enf.... |
| QLOC52 | - |  |  | SI | Otra (Especifique) |
| QLOC54 | - |  |  | SI | País |
| QOBS55 | - |  |  | SI | Observaciones |
| QPC53 | - |  |  | SI | País de Contagio |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*