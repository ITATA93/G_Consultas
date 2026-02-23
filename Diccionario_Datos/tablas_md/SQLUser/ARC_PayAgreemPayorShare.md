# SQLUser.ARC_PayAgreemPayorShare

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYOR_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| PAYOR_AgeFrom | double |  |  | SI | AgeFrom |
| PAYOR_AgeTo | double |  |  | SI | AgeTo |
| PAYOR_Childsub | double |  |  | NO | Childsub |
| PAYOR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAYOR_CreatedDate | date |  |  | SI | Created Date |
| PAYOR_CreatedTime | time |  |  | SI | Created Time |
| PAYOR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAYOR_DiagnosisGroup1_DR | bigint |  | FK | SI | Des Ref DiagnosisGroup1 |
| PAYOR_EpisodeType | varchar |  |  | SI | Episode Type |
| PAYOR_PayorShare | double |  |  | SI | PayorShare |
| PAYOR_Rank | double |  |  | SI | Rank |
| PAYOR_RowId | varchar |  |  | NO | - |
| PAYOR_UpdatedDate | date |  |  | SI | Updated Date |
| PAYOR_UpdatedTime | time |  |  | SI | Updated Time |
| PAYOR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Escala de Severidad |
| Q02 | - |  |  | SI | El paciente presenta o puede presentar alguna de e... |
| Q03 | - |  |  | SI | Nivel 7 (N7) |
| Q04 | - |  |  | SI | - Deglución normal en todos los casos |
| Q05 | - |  |  | SI | Nivel 6 (N6) |
| Q06 | - |  |  | SI | - Leve atraso oral o faríngeo, estancamiento o res... |
| Q07 | - |  |  | SI | - Puede necesitar de tiempo extra para las comidas... |
| Q08 | - |  |  | SI | Nivel 5 (N5) |
| Q09 | - |  |  | SI | - Aspiración solamente de líquidos, pero con un fu... |
| Q10 | - |  |  | SI | - Penetración sobre los pliegues vocales con una o... |
| Q11 | - |  |  | SI | - Estancamiento en la faringe, y que despeja espon... |
| Q12 | - |  |  | SI | Nivel 4 (N4) |
| Q13 | - |  |  | SI | - Estancamiento en la faringe, despeja con orienta... |
| Q14 | - |  |  | SI | - Aspiración con una consistencia, con reflejo de ... |
| Q15 | - |  |  | SI | - La penetración a nivel de los pliegues vocales c... |
| Q16 | - |  |  | SI | - La penetración a nivel de los pliegues vocales s... |
| Q17 | - |  |  | SI | Nivel 3 (N3) |
| Q18 | - |  |  | SI | - Estancamiento moderado de la faringe, despeje co... |
| Q19 | - |  |  | SI | - Estancamiento moderado en la cavidad oral, despe... |
| Q20 | - |  |  | SI | - Nivel de penetración en los pliegues vocales sin... |
| Q21 | - |  |  | SI | - Aspiración de dos consistencias, con reflejo de ... |
| Q22 | - |  |  | SI | - Aspiración de una consistencia, sin tos ni penet... |
| Q23 | - |  |  | SI | Nivel 2 (N2) |
| Q24 | - |  |  | SI | - Estancamiento grave en la faringe, incapacidad d... |
| Q25 | - |  |  | SI | - Estancamiento grave o pérdida del bolo en fase o... |
| Q26 | - |  |  | SI | - Aspiración con dos o más consistencias, sin refl... |
| Q27 | - |  |  | SI | Nivel 1 (N1) |
| Q28 | - |  |  | SI | - Estancamiento severo en la faringe, siendo incap... |
| Q29 | - |  |  | SI | - Estancamiento o pérdida de bolo en forma oral se... |
| Q30 | - |  |  | SI | - Aspiración silenciosa con dos o más consistencia... |
| Q31 | - |  |  | SI | VÍA ORAL SUSPENDIDA - NECESIDAD DE NUTRICÓN NO ORA... |
| Q32 | - |  |  | SI | VÍA ORAL SUSPENDIDA - NECESIDAD DE NUTRICÓN NO ORA... |
| Q33 | - |  |  | SI | Máxima asistencia de uso de estrategias con vía or... |
| Q34 | - |  |  | SI | DIETA POR VÍA ORAL MODIFICADA Y/O INDEPENDIENTE.&n... |
| Q35 | - |  |  | SI | Total asistencia, supervisión o estrategia, restri... |
| Q36 | - |  |  | SI | DIETA POR VÍA ORAL MODIFICADA Y/O INDEPENDIENTE. |
| Q37 | - |  |  | SI | Supervisión a distancia, puede necesitar de restri... |
| Q38 | - |  |  | SI | DIETA NORMAL POR VÏA ORAL. |
| Q39 | - |  |  | SI | Ninguna estrategia o tiempo extra necesario |
| Q40 | - |  |  | SI | DIETA POR VÍA ORAL MODIFICADA Y/O INDEPENDIENTE. |
| Q41 | - |  |  | SI | Supervisión a distancia, puede necesitar de restri... |
| Q42 | - |  |  | SI | DIETA NORMAL POR VÏA ORAL. |
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