# questionnaire.QTCECLAECO

> Ecografía Obstétrica

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ecografía Obstétrica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | Procedencia |
| Q04 | varchar |  |  | SI | Indicación |
| Q05 | varchar |  |  | SI | Saco gestacional |
| Q06 | numeric |  |  | SI | Diámetro promedio del saco g. |
| Q07 | varchar |  |  | SI | Concepto |
| Q08 | varchar |  |  | SI | Latido cardíaco fetal |
| Q09 | numeric |  |  | SI | Longitud céfalo-nalgas |
| Q10 | varchar |  |  | SI | Presentación |
| Q11 | varchar |  |  | SI | Dorso |
| Q12 | varchar |  |  | SI | Diametro biparietal DBP |
| Q12ObsDR | varchar |  | FK | SI | Diametro biparietal DBP DR |
| Q13 | numeric |  |  | SI | Diametro fronto-occipital DFO mm |
| Q14 | varchar |  |  | SI | Sexo |
| Q15 | varchar |  |  | SI | Perímetro abdominal |
| Q15ObsDR | varchar |  | FK | SI | Perímetro abdominal DR |
| Q16 | numeric |  |  | SI | Fémur |
| Q17 | varchar |  |  | SI | Placenta (posición) |
| Q18 | varchar |  |  | SI | Placenta (Grado de maduración) |
| Q19 | varchar |  |  | SI | Líquido amniótico (volumen) |
| Q20 | varchar |  |  | SI | Comentario |
| Q21 | varchar |  |  | SI | Conclusión |
| Q22 | varchar |  |  | SI | Imagen |
| Q23 | bigint |  |  | SI | Foto o texto |
| Q23TxtOnly | bigint |  |  | SI | Foto o texto Plain Text Only |
| Q24 | varchar |  |  | SI | Edad gestacional |
| Q24ObsDR | varchar |  | FK | SI | Edad gestacional DR |
| Q25 | varchar |  |  | SI | Peso estimado del feto |
| Q25ObsDR | varchar |  | FK | SI | Peso estimado del feto DR |
| Q27 | varchar |  |  | SI | Presenta Malformación congénita |
| Q28 | varchar |  |  | SI | Latidos por Minuto |
| Q28ObsDR | varchar |  | FK | SI | Latidos por Minuto DR |
| Q32 | varchar |  |  | SI | Cabeza |
| Q33 | varchar |  |  | SI | Corazón |
| Q34 | varchar |  |  | SI | Columna |
| Q35 | varchar |  |  | SI | Abdomen |
| Q36 | varchar |  |  | SI | Riñones y Vejiga |
| Q37 | varchar |  |  | SI | Extremidades |
| Q38 | varchar |  |  | SI | Posición  |
| Q39 | varchar |  |  | SI | Ubicación de la Placenta (Pared /Cara) |
| Q40 | numeric |  |  | SI | Índice Líquido Amniótico |
| Q41 | varchar |  |  | SI | Cordón Umbilical |
| Q42 | varchar |  |  | SI | Percentil Cony Alarcón y Pittaluga |
| QRE | varchar |  |  | SI | Establecimiento de Realización de la Ecografía |
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