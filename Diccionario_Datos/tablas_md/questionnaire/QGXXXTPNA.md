# questionnaire.QGXXXTPNA

> Nutrición Parenteral Adulto

**Schema:** questionnaire
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nutrición Parenteral Adulto

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Talla |
| Q01ObsDR | varchar |  | FK | SI | Talla DR |
| Q02 | varchar |  |  | SI | Peso |
| Q02ObsDR | varchar |  | FK | SI | Peso DR |
| Q03 | varchar |  |  | SI | Indicación de Nutrición Parenteral |
| Q04 | varchar |  |  | SI | Instrucciones |
| Q05 | varchar |  |  | SI | Ruta de Administración |
| Q07 | varchar |  |  | SI | Solución Base |
| Q08 | numeric |  |  | SI | Dextrosa (g) |
| Q09 | numeric |  |  | SI | Aminoácidos (g) |
| Q10 | varchar |  |  | SI | Marca aminoácidos |
| Q11 | varchar |  |  | SI | Para pacientes con VVP y tolerancia a la glucosa e... |
| Q12 | numeric |  |  | SI | Kcal |
| Q13 | numeric |  |  | SI | Velocidad de infusión máxima, no exceder los (ml/h... |
| Q14 | numeric |  |  | SI | Osmolaridad final de la NP igual o menor a&nbsp;(m... |
| Q15 | varchar |  |  | SI | La Nutrición Parenteral DEBE ser administrada a tr... |
| Q16 | varchar |  |  | SI | Emulsión lipídica - vía infusión periférica o CVC ... |
| Q17 | varchar |  |  | SI | Para pacientes con CVC o PICC y tolerancia a la gl... |
| Q18 | varchar |  |  | SI | Densidad |
| Q19 | varchar |  |  | SI | Volumen |
| Q20 | varchar |  |  | SI | Para pacientes con CVC o PICC y tolerancia a gluco... |
| Q21 | numeric |  |  | SI | Aminoácidos (g) |
| Q22 | varchar |  |  | SI | Amino acids brand |
| Q23 | numeric |  |  | SI | Emulsión&nbsp;lipídica (g) |
| Q24 | varchar |  |  | SI | Fat emulsion brand |
| Q25 | varchar |  |  | SI | Aditivos: (por día) |
| Q26 | numeric |  |  | SI | Cloruro de Sodio |
| Q27 | numeric |  |  | SI | - como Acetato (mEq) |
| Q28 | numeric |  |  | SI | - como Fosfato (mmol de PO4) |
| Q29 | numeric |  |  | SI | Cloruro de Potasio&nbsp;(mEq) |
| Q30 | numeric |  |  | SI | - como Acetato (mEq) |
| Q31 | numeric |  |  | SI | - como Fosfato (mmol de PO4) |
| Q32 | numeric |  |  | SI | Gluconato de Calcio (mEq) |
| Q33 | numeric |  |  | SI | Sulfato de Magnesio&nbsp;(mEq) |
| Q34 | numeric |  |  | SI | Oligoelementos&nbsp;(mL/día) |
| Q35 | numeric |  |  | SI | Multivitaminas Adulto (mL/día) |
| Q36 | varchar |  |  | SI | Antagonista H2 |
| Q37 | numeric |  |  | SI | (mg) |
| Q38 | varchar |  |  | SI | Otro: |
| Q39 | varchar |  |  | SI | Dosis normales |
| Q40 | varchar |  |  | SI | 1-2 mEq Sodio/Kg/día |
| Q41 | varchar |  |  | SI | pH o Co2 dependiente |
| Q42 | varchar |  |  | SI | Considerar en caso de hiperkalemia |
| Q43 | varchar |  |  | SI | 1-2 mEq Potasio/kg/día |
| Q44 | varchar |  |  | SI | pH o CO2 dependiente |
| Q45 | varchar |  |  | SI | 20-40 mmol/día (1 mmol Phos = 1.5 mEq K) |
| Q46 | varchar |  |  | SI | 5-15 mEq/día |
| Q47 | varchar |  |  | SI | 8-24 mEq/día |
| Q48 | varchar |  |  | SI | Contiene vitamina K 150 mcg |
| Q49 | numeric |  |  | SI | mg/día con función renal normal |
| Q50 | numeric |  |  | SI | Zn (mg) |
| Q51 | numeric |  |  | SI | Cu (mg) |
| Q52 | numeric |  |  | SI | Mn (mg) |
| Q53 | numeric |  |  | SI | Cr (mcg) |
| Q54 | numeric |  |  | SI | Se (mcg) |
| Q55 | varchar |  |  | SI | (con función hepática normal) |
| Q56 | numeric |  |  | SI | Insulina regular (UI) |
| Q57 | varchar |  |  | SI | Recomendado en caso de hiperglicemia, iniciar con ... |
| Q58 | varchar |  |  | SI | Emulsión Lipídica (Marca) |
| Q59 | bit |  |  | SI | Vía Venosa Periférica (VVP) |
| Q60 | bit |  |  | SI | CVC o PICC |
| Q61 | varchar |  |  | SI | Vía de Administración |
| Q62 | date |  |  | SI | Fecha |
| Q63 | time |  |  | SI | Hora |
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