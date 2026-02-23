# SQLUser.AR_HICInHospitalClaimRepRow

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IHCRR_ParRef | bigint | PK |  | NO | - |
| IHCRR_ElementName | varchar |  |  | NO | Name of the element |
| IHCRR_ElementValue | varchar |  |  | SI | Value of the element |
| IHCRR_InHospitalClaim_DR | bigint |  | FK | SI | IHC for this report row |
| IHCRR_RowID | varchar |  |  | NO | - |
| IHCRR_RowNumber | integer |  |  | NO | Row number |
| Q01 | - |  |  | SI | ... se sintió bien o con el ánimo tan elevado, o t... |
| Q02 | - |  |  | SI | ... estaba tan irritable, que le gritaba a la gent... |
| Q03 | - |  |  | SI | ... se sentía mucho más seguro de sí mismo que otr... |
| Q04 | - |  |  | SI | ... dormía mucho menos que de costumbre, pero nota... |
| Q05 | - |  |  | SI | ... hablaba mucho más, o mucho más rápido que de c... |
| Q06 | - |  |  | SI | ... le pasaban las ides muy rápidamente por la cab... |
| Q07 | - |  |  | SI | ... se distraía muy fácilmente por las cosas que s... |
| Q08 | - |  |  | SI | ... tenía más energía que de costumbre? |
| Q09 | - |  |  | SI | ... estaba mucho más activo o hacía muchas más cos... |
| Q10 | - |  |  | SI | ... era socialmente mucho más activo y comunicativ... |
| Q11 | - |  |  | SI | ... se interesaba en el sexo más que de costumbre? |
| Q12 | - |  |  | SI | ... hacía cosas que no eran comunes en usted, o qu... |
| Q13 | - |  |  | SI | ... el gastar dinero le causó problemas a usted o ... |
| Q14 | - |  |  | SI | ¿Ocurrieron varias de esas situaciones juntas en u... |
| Q15 | - |  |  | SI | ¿Cuantas dificultades le causaron cualquiera de la... |
| Q16 | - |  |  | SI | ¿Alguno de sus familiares directos (es decir, hijo... |
| Q17 | - |  |  | SI | ¿Le ha dicho alguna vez un profesional médico que ... |
| Q18 | - |  |  | SI | ¿Le sucedió alguna vez que por un cierto período d... |
| Q19 | - |  |  | SI | Si usted marcó SI más de una vez |
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