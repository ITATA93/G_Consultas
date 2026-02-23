# SQLUser.ARC_PayAgreemBulkBillIncent

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBINC_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| BBINC_Childsub | double |  |  | NO | Childsub |
| BBINC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BBINC_CreatedDate | date |  |  | SI | Created Date |
| BBINC_CreatedTime | time |  |  | SI | Created Time |
| BBINC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BBINC_DateFrom | date |  |  | SI | Date From |
| BBINC_DateTo | date |  |  | SI | Date To |
| BBINC_ItemCat_DR | bigint |  | FK | SI | Des Ref ARCItemCat |
| BBINC_Percentage | double |  |  | SI | % Percentage |
| BBINC_RowId | varchar |  |  | NO | - |
| BBINC_Tariff_DR | bigint |  | FK | SI | Des Ref ARCTariff |
| BBINC_UpdatedDate | date |  |  | SI | Updated Date |
| BBINC_UpdatedTime | time |  |  | SI | Updated Time |
| BBINC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | 1- Siento que tengo pocas cosas buenas para ofrece... |
| Q04 | - |  |  | SI | 2. Parece que mi vida no tiene sentido |
| Q05 | - |  |  | SI | 3. Siento que mi papel en la vida se ha perdido |
| Q06 | - |  |  | SI | 4. Siento que ya no controlo mis emociones |
| Q07 | - |  |  | SI | 5. Siento que nadie puede ayudarme |
| Q08 | - |  |  | SI | 6. Siento que no puedo ayudarme |
| Q09 | - |  |  | SI | 7. Me siento desesperanzado(a) |
| Q10 | - |  |  | SI | 8. Me siento irritable |
| Q11 | - |  |  | SI | 9. Siento que no afronto bien la vida |
| Q12 | - |  |  | SI | 10. Me arrepiento de muchas cosas en la vida |
| Q13 | - |  |  | SI | 11. Tiendo a sentirme fácilmente afectado(a) en el... |
| Q14 | - |  |  | SI | 12. Me siento afligido/acongojado por lo que me es... |
| Q15 | - |  |  | SI | 13. Soy una persona que no vale la pena |
| Q16 | - |  |  | SI | 14. Preferiría no estar vivo(a) |
| Q17 | - |  |  | SI | 15. Me siento muy solo(a) o aislado(a) |
| Q18 | - |  |  | SI | 16. Me siento atrapado(a) por lo que me está pasan... |
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