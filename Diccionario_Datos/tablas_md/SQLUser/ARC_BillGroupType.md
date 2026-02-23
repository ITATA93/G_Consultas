# SQLUser.ARC_BillGroupType

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BILLGT_RowId | bigint | PK |  | NO | - |
| BILLGT_Code | varchar |  |  | NO | Code |
| BILLGT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BILLGT_CreatedDate | date |  |  | SI | Created Date |
| BILLGT_CreatedTime | time |  |  | SI | Created Time |
| BILLGT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BILLGT_Default | varchar |  |  | SI | Default |
| BILLGT_Desc | varchar |  |  | NO | Description |
| BILLGT_EndDate | date |  |  | SI | End Date |
| BILLGT_Owner | varchar |  |  | SI | Owner |
| BILLGT_StartDate | date |  |  | SI | Start Date |
| BILLGT_Type | varchar |  |  | SI | Type |
| BILLGT_UpdatedDate | date |  |  | SI | Updated Date |
| BILLGT_UpdatedTime | time |  |  | SI | Updated Time |
| BILLGT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Procedencia |
| Q04 | - |  |  | SI | Indicación |
| Q05 | - |  |  | SI | Saco gestacional |
| Q06 | - |  |  | SI | Diámetro promedio del saco g. |
| Q07 | - |  |  | SI | Concepto |
| Q08 | - |  |  | SI | Latido cardíaco fetal |
| Q09 | - |  |  | SI | Longitud céfalo-nalgas |
| Q10 | - |  |  | SI | Presentación |
| Q11 | - |  |  | SI | Dorso |
| Q12 | - |  |  | SI | Diametro biparietal DBP |
| Q12ObsDR | - |  |  | SI | Diametro biparietal DBP DR |
| Q13 | - |  |  | SI | Diametro fronto-occipital DFO mm |
| Q14 | - |  |  | SI | Sexo |
| Q15 | - |  |  | SI | Perímetro abdominal |
| Q15ObsDR | - |  |  | SI | Perímetro abdominal DR |
| Q16 | - |  |  | SI | Fémur |
| Q17 | - |  |  | SI | Placenta (posición) |
| Q18 | - |  |  | SI | Placenta (Grado de maduración) |
| Q19 | - |  |  | SI | Líquido amniótico (volumen) |
| Q20 | - |  |  | SI | Comentario |
| Q21 | - |  |  | SI | Conclusión |
| Q22 | - |  |  | SI | Imagen |
| Q23 | - |  |  | SI | Foto o texto |
| Q23TxtOnly | - |  |  | SI | Foto o texto Plain Text Only |
| Q24 | - |  |  | SI | Edad gestacional |
| Q24ObsDR | - |  |  | SI | Edad gestacional DR |
| Q25 | - |  |  | SI | Peso estimado del feto |
| Q25ObsDR | - |  |  | SI | Peso estimado del feto DR |
| Q27 | - |  |  | SI | Presenta Malformación congénita |
| Q28 | - |  |  | SI | Latidos por Minuto |
| Q28ObsDR | - |  |  | SI | Latidos por Minuto DR |
| Q32 | - |  |  | SI | Cabeza |
| Q33 | - |  |  | SI | Corazón |
| Q34 | - |  |  | SI | Columna |
| Q35 | - |  |  | SI | Abdomen |
| Q36 | - |  |  | SI | Riñones y Vejiga |
| Q37 | - |  |  | SI | Extremidades |
| Q38 | - |  |  | SI | Posición |
| Q39 | - |  |  | SI | Ubicación de la Placenta (Pared /Cara) |
| Q40 | - |  |  | SI | Índice Líquido Amniótico |
| Q41 | - |  |  | SI | Cordón Umbilical |
| Q42 | - |  |  | SI | Percentil Cony Alarcón y Pittaluga |
| QRE | - |  |  | SI | Establecimiento de Realización de la Ecografía |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*