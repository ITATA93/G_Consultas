# lab.CR_BatchLinePatients

**Schema:** lab
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRBLB_ParRef | varchar | PK |  | NO | CR_BatchLine Parent Reference |
| CRBLB_Amount | double |  |  | SI | Amount to credit |
| CRBLB_AmountInCredit | double |  |  | SI | Amount In Credit |
| CRBLB_AmountOriginal | double |  |  | SI | Original Amount |
| CRBLB_BillLocation_DR | varchar |  | FK | SI | Bill Location DR |
| CRBLB_Calculation | varchar |  |  | SI | Calculation |
| CRBLB_Company_DR | varchar |  | FK | SI | Company DR |
| CRBLB_DateOfCollection | date |  |  | SI | Date Of Collection |
| CRBLB_DateOfPosting | date |  |  | SI | Date Of Posting |
| CRBLB_DebtorNumber_DR | varchar |  | FK | SI | Debtor Number DR |
| CRBLB_Flag | varchar |  |  | SI | Flag |
| CRBLB_RowID | varchar |  |  | NO | - |
| CRBLB_Visit_DR | varchar |  | FK | NO | Visit DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*