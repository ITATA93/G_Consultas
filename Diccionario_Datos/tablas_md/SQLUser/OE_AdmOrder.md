# SQLUser.OE_AdmOrder

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMORD_RowId | bigint | PK |  | NO | - |
| ADMORD_EndDate | date |  |  | SI | Latest Order End Date |
| ADMORD_PAADM_DR | bigint |  | FK | SI | Des Ref PAAdm |
| ADMORD_StartDate | date |  |  | SI | Earliest Order Start Date |
| Q01 | - |  |  | SI | Talla |
| Q01ObsDR | - |  |  | SI | Talla DR |
| Q02 | - |  |  | SI | Peso |
| Q02ObsDR | - |  |  | SI | Peso DR |
| Q03 | - |  |  | SI | Indicación de Nutrición Parenteral |
| Q04 | - |  |  | SI | Instrucciones |
| Q05 | - |  |  | SI | Ruta de Administración |
| Q07 | - |  |  | SI | Solución Base |
| Q08 | - |  |  | SI | Dextrosa (g) |
| Q09 | - |  |  | SI | Aminoácidos (g) |
| Q10 | - |  |  | SI | Marca aminoácidos |
| Q11 | - |  |  | SI | Para pacientes con VVP y tolerancia a la glucosa e... |
| Q12 | - |  |  | SI | Kcal |
| Q13 | - |  |  | SI | Velocidad de infusión máxima, no exceder los (ml/h... |
| Q14 | - |  |  | SI | Osmolaridad final de la NP igual o menor a&nbsp |
| Q15 | - |  |  | SI | La Nutrición Parenteral DEBE ser administrada a tr... |
| Q16 | - |  |  | SI | Emulsión lipídica - vía infusión periférica o CVC ... |
| Q17 | - |  |  | SI | Para pacientes con CVC o PICC y tolerancia a la gl... |
| Q18 | - |  |  | SI | Densidad |
| Q19 | - |  |  | SI | Volumen |
| Q20 | - |  |  | SI | Para pacientes con CVC o PICC y tolerancia a gluco... |
| Q21 | - |  |  | SI | Aminoácidos (g) |
| Q22 | - |  |  | SI | Amino acids brand |
| Q23 | - |  |  | SI | Emulsión&nbsp |
| Q24 | - |  |  | SI | Fat emulsion brand |
| Q25 | - |  |  | SI | Aditivos: (por día) |
| Q26 | - |  |  | SI | Cloruro de Sodio |
| Q27 | - |  |  | SI | - como Acetato (mEq) |
| Q28 | - |  |  | SI | - como Fosfato (mmol de PO4) |
| Q29 | - |  |  | SI | Cloruro de Potasio&nbsp |
| Q30 | - |  |  | SI | - como Acetato (mEq) |
| Q31 | - |  |  | SI | - como Fosfato (mmol de PO4) |
| Q32 | - |  |  | SI | Gluconato de Calcio (mEq) |
| Q33 | - |  |  | SI | Sulfato de Magnesio&nbsp |
| Q34 | - |  |  | SI | Oligoelementos&nbsp |
| Q35 | - |  |  | SI | Multivitaminas Adulto (mL/día) |
| Q36 | - |  |  | SI | Antagonista H2 |
| Q37 | - |  |  | SI | (mg) |
| Q38 | - |  |  | SI | Otro: |
| Q39 | - |  |  | SI | Dosis normales |
| Q40 | - |  |  | SI | 1-2 mEq Sodio/Kg/día |
| Q41 | - |  |  | SI | pH o Co2 dependiente |
| Q42 | - |  |  | SI | Considerar en caso de hiperkalemia |
| Q43 | - |  |  | SI | 1-2 mEq Potasio/kg/día |
| Q44 | - |  |  | SI | pH o CO2 dependiente |
| Q45 | - |  |  | SI | 20-40 mmol/día (1 mmol Phos = 1.5 mEq K) |
| Q46 | - |  |  | SI | 5-15 mEq/día |
| Q47 | - |  |  | SI | 8-24 mEq/día |
| Q48 | - |  |  | SI | Contiene vitamina K 150 mcg |
| Q49 | - |  |  | SI | mg/día con función renal normal |
| Q50 | - |  |  | SI | Zn (mg) |
| Q51 | - |  |  | SI | Cu (mg) |
| Q52 | - |  |  | SI | Mn (mg) |
| Q53 | - |  |  | SI | Cr (mcg) |
| Q54 | - |  |  | SI | Se (mcg) |
| Q55 | - |  |  | SI | (con función hepática normal) |
| Q56 | - |  |  | SI | Insulina regular (UI) |
| Q57 | - |  |  | SI | Recomendado en caso de hiperglicemia, iniciar con ... |
| Q58 | - |  |  | SI | Emulsión Lipídica (Marca) |
| Q59 | - |  |  | SI | Vía Venosa Periférica (VVP) |
| Q60 | - |  |  | SI | CVC o PICC |
| Q61 | - |  |  | SI | Vía de Administración |
| Q62 | - |  |  | SI | Fecha |
| Q63 | - |  |  | SI | Hora |
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