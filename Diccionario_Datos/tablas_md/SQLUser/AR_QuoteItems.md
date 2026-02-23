# SQLUser.AR_QuoteItems

**Schema:** SQLUser
**Columnas:** 133
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | AR_Quote Parent Reference |
| ChildQ41DR | - |  |  | SI | Child Reference: Grupo familiar |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ITM_Accommodation | varchar |  |  | SI | Accommodation Flag |
| ITM_ApprovalRequestAmount | double |  |  | SI | Approval Request Amount |
| ITM_AuthClin_DR | varchar |  | FK | SI | Des Ref CTCareProv - Authorising Clinician |
| ITM_BillItemKey | varchar |  |  | SI | BillItemKey |
| ITM_BillsTotalAmt | double |  |  | SI | Bills Total Amt |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CopaymentAmt | double |  |  | SI | CopaymentAmt |
| ITM_DaysStay | double |  |  | SI | DaysStay |
| ITM_Excess | double |  |  | SI | Excess |
| ITM_InsTypeApprovLimit_DR | varchar |  | FK | SI | Des Ref ARCInsTypeApprovalLimits |
| ITM_LimitExceeded | varchar |  |  | SI | Limit Exceeded Flag |
| ITM_OrdLoc_DR | bigint |  | FK | SI | Des Ref CTLoc - Ordering Location |
| ITM_OrdSetDate_DR | varchar |  | FK | SI | Des Ref to ARCOrdSetDate |
| ITM_OrdSet_DR | varchar |  | FK | SI | Des Ref to ARCOrdSets |
| ITM_PatientAmt | double |  |  | SI | PatientAmt |
| ITM_PatientDesc | varchar |  |  | SI | PatientDesc |
| ITM_PayAgreemApprovLimit_DR | varchar |  | FK | SI | Des Ref ARCPayAgreemApprovalLimits |
| ITM_PayorAmt | double |  |  | SI | PayorAmt |
| ITM_PayorDesc | varchar |  |  | SI | PayorDesc |
| ITM_PayorKey | varchar |  |  | SI | PayorKey |
| ITM_Price | double |  |  | SI | Price |
| ITM_PriceBeforeDiscount | double |  |  | SI | PriceBeforeDiscount |
| ITM_PrintDate | date |  |  | SI | PrintDate |
| ITM_PrintTime | time |  |  | SI | PrintTime |
| ITM_Qty | double |  |  | SI | Qty |
| ITM_RecLoc_DR | bigint |  | FK | SI | Des Ref CTLoc - Receiving Location |
| ITM_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_ServTax_DR | bigint |  | FK | SI | Des Ref to ARCST |
| ITM_ServiceTax | double |  |  | SI | ServiceTax |
| ITM_ToothText1 | varchar |  |  | SI | Tooth Text1 |
| ITM_ToothText2 | varchar |  |  | SI | Tooth Text2 |
| ITM_ToothText3 | varchar |  |  | SI | Tooth Text3 |
| ITM_ToothText4 | varchar |  |  | SI | Tooth Text4 |
| ITM_ToothText5 | varchar |  |  | SI | Tooth Text5 |
| ITM_Type | varchar |  |  | SI | Type |
| Q01 | - |  |  | SI | 1. Identificacion Individual |
| Q02 | - |  |  | SI | Nombre |
| Q03 | - |  |  | SI | Sexo |
| Q04 | - |  |  | SI | Fecha de Nacimiento |
| Q05 | - |  |  | SI | Edad |
| Q06 | - |  |  | SI | RUN |
| Q07 | - |  |  | SI | N° de Hijos |
| Q08 | - |  |  | SI | Educacion |
| Q09 | - |  |  | SI | Actividad |
| Q10 | - |  |  | SI | Otra Actividad |
| Q11 | - |  |  | SI | Domicilio |
| Q12 | - |  |  | SI | Comuna |
| Q13 | - |  |  | SI | N° Ficha Clínica |
| Q14 | - |  |  | SI | Centro de Salud de su Domicilio |
| Q15 | - |  |  | SI | 2. Relativos a Intento de Suicidio |
| Q16 | - |  |  | SI | Fecha de Intento de Suicidio |
| Q17 | - |  |  | SI | Causa |
| Q18 | - |  |  | SI | Método utilizado en el intento |
| Q19 | - |  |  | SI | Fue derivada/o a Psiquiatra después del intento |
| Q20 | - |  |  | SI | Fue derivado a Equipo de Salud Mental del Centro d... |
| Q21 | - |  |  | SI | ¿Cuál? |
| Q22 | - |  |  | SI | Establecimiento de Salud donde se realiza la atenc... |
| Q23 | - |  |  | SI | En caso que no recibio atencion en un Establecimie... |
| Q24 | - |  |  | SI | Profesor |
| Q25 | - |  |  | SI | Carabinero |
| Q26 | - |  |  | SI | Otro |
| Q27 | - |  |  | SI | 3. Antecedentes de Salud de la Persona con Intento... |
| Q28 | - |  |  | SI | Padece de enfermedad física |
| Q29 | - |  |  | SI | Padece de enfermedad mental |
| Q30 | - |  |  | SI | Esta en tratamiento por la enfermedad mental |
| Q31 | - |  |  | SI | En que Establecimiento está en tratamiento por la ... |
| Q32 | - |  |  | SI | Consume drogas |
| Q33 | - |  |  | SI | Maltrato infantil |
| Q34 | - |  |  | SI | VIF |
| Q35 | - |  |  | SI | 4.  Relativos a la Persona con Intento de Suicidio... |
| Q36 | - |  |  | SI | La persona individualizada ha realizado con anteri... |
| Q37 | - |  |  | SI | Intentos de Suicidios |
| Q38 | - |  |  | SI | ¿Cuántos? |
| Q39 | - |  |  | SI | Hay intentos de suicidio en la familia |
| Q40 | - |  |  | SI | Hay suicidios en la familia |
| Q42 | - |  |  | SI | 5. Familiar que estaría dispuesta/o a entregar may... |
| Q43 | - |  |  | SI | Nombre |
| Q44 | - |  |  | SI | Telefono |
| Q45 | - |  |  | SI | Direccion |
| Q46 | - |  |  | SI | 6. Funcionario responsable de la Informacion |
| Q47 | - |  |  | SI | Nombre Completo |
| Q48 | - |  |  | SI | RUN |
| Q49 | - |  |  | SI | Cargo |
| Q50 | - |  |  | SI | Establecimiento |
| Q51 | - |  |  | SI | Comuna |
| Q52 | - |  |  | SI | Fecha |
| Q53 | - |  |  | SI | Apellido Paterno |
| Q54 | - |  |  | SI | Apellido Materno |
| Q55 | - |  |  | SI | ¿Qué funcionario/s realiza la atencion de urgencia... |
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