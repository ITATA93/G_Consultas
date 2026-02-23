# SQLUser.LBC_TMParameter

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTMP_RowID | bigint | PK |  | NO | - |
| LBCTMP_AllowEI | varchar |  |  | SI | Allow Electronic Issue |
| LBCTMP_AllowValidateProductExpiryUpdate | varchar |  |  | SI | Allow 'validate' to update product expiry/time |
| LBCTMP_AutoDisposalCode_DR | bigint |  | FK | SI | Disposal Code for auto disposal of Autologous/Dire... |
| LBCTMP_BloodIssueReportGroup_DR | bigint |  | FK | SI | Blood Issue Report Group |
| LBCTMP_BloodPackDINLabel_DR | bigint |  | FK | SI | The report to use to produce the barcode-label of ... |
| LBCTMP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTMP_ControlledIssue | varchar |  |  | SI | Controlled Issue In Use |
| LBCTMP_CreatedDate | date |  |  | SI | Created Date |
| LBCTMP_CreatedTime | time |  |  | SI | Created Time |
| LBCTMP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTMP_EDNDestinationID | varchar |  |  | SI | Electronic Delivery Note Destination ID
Links EDN... |
| LBCTMP_EmergencyIssueOnSuitSampleFail | varchar |  |  | SI | Enforce Emergency Issue of Crossmatch products if ... |
| LBCTMP_EnableRapidBPEntryDefaults | varchar |  |  | SI | Enable Rapid Blood Product Entry Defaults
On Elec... |
| LBCTMP_EnableStrictLabelVerification | varchar |  |  | SI | Enforce Strict Label Verification on Barcode scann... |
| LBCTMP_ExpiredAutoDisposalCode_DR | bigint |  | FK | SI | Disposal code for auto fated expired units |
| LBCTMP_LabSite_DR | bigint |  | FK | SI | Lab Site Location.  Optional |
| LBCTMP_LabelVerification | varchar |  |  | SI | Label Verification In Use |
| LBCTMP_MaxSuitabilityPeriodExtension | numeric |  |  | SI | Maximum specimen suitability extension period (day... |
| LBCTMP_NeonatalAge | numeric |  |  | SI | Age of patient (up to) to be processed as neonatal... |
| LBCTMP_Owner | varchar |  |  | SI | Owner |
| LBCTMP_PreviousIncompatAction | varchar |  |  | SI | Previous Incompatibility Action |
| LBCTMP_SuitabilityPeriodValidToEndOfExpiryDay | varchar |  |  | SI | Allows suitability periods to be valid until 23:59... |
| LBCTMP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTMP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTMP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha de realización |
| Q02 | - |  |  | SI | Hora de realización |
| Q03 | - |  |  | SI | Indicación |
| Q04 | - |  |  | SI | FUR |
| Q05 | - |  |  | SI | Gestaciones |
| Q06 | - |  |  | SI | Partos |
| Q07 | - |  |  | SI | Transductor |
| Q08 | - |  |  | SI | Vejiga |
| Q09 | - |  |  | SI | Posición |
| Q10 | - |  |  | SI | Ubicación |
| Q11 | - |  |  | SI | Forma |
| Q12 | - |  |  | SI | Borde |
| Q13 | - |  |  | SI | Patrón Miometrial |
| Q14 | - |  |  | SI | Cuerpo Longitud (cms.) |
| Q15 | - |  |  | SI | Transverso (cms.) |
| Q16 | - |  |  | SI | Antero-Posterior (cms.) |
| Q17 | - |  |  | SI | Observaciones (útero) |
| Q18 | - |  |  | SI | Endometrio |
| Q19 | - |  |  | SI | Grosor (mms.) |
| Q20 | - |  |  | SI | Observaciones (Endometrio) |
| Q21 | - |  |  | SI | Fondo de saco de Douglas |
| Q22 | - |  |  | SI | Anexos |
| Q23 | - |  |  | SI | Longitud OD |
| Q24 | - |  |  | SI | Longitud OI |
| Q25 | - |  |  | SI | Transv. OD |
| Q26 | - |  |  | SI | Transv. OI |
| Q27 | - |  |  | SI | AP OD |
| Q28 | - |  |  | SI | AP OI |
| Q29 | - |  |  | SI | Volumen OD |
| Q30 | - |  |  | SI | Volumen OI |
| Q31 | - |  |  | SI | Otros Hallazgos |
| Q32 | - |  |  | SI | Observaciones Generales |
| Q33 | - |  |  | SI | Conclusión Ecográfica |
| Q34 | - |  |  | SI | Profesional que Realiza |
| Q35 | - |  |  | SI | Imagen |
| Q35TxtOnly | - |  |  | SI | Imagen Plain Text Only |
| Q36 | - |  |  | SI | Vejiga |
| Q37 | - |  |  | SI | Endometrio |
| Q38 | - |  |  | SI | Ovarios |
| Q39 | - |  |  | SI | Antecedentes Ginecológicos |
| Q40 | - |  |  | SI | Medidas |
| Q41 | - |  |  | SI | Vejiga |
| Q42 | - |  |  | SI | Fondo de Saco de Douglas |
| Q43 | - |  |  | SI | Utero |
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