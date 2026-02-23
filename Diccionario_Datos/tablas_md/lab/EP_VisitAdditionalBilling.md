# lab.EP_VisitAdditionalBilling

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISAB_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISAB_Amount | double |  |  | SI | Amount |
| VISAB_AmountPerUnit | double |  |  | SI | AmountPerUnit |
| VISAB_Description | varchar |  |  | SI | Description |
| VISAB_InitiationCode_DR | varchar |  | FK | SI | Initiation Code DR |
| VISAB_PaymentCode_DR | varchar |  | FK | SI | Payment Code DR |
| VISAB_RowID | varchar |  |  | NO | - |
| VISAB_Sequence | double |  |  | NO | Sequence |
| VISAB_Units | double |  |  | SI | Units |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*