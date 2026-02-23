# lab.CTBB_TransactionUserGroup

**Schema:** lab
**Columnas:** 3
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBTRU_ParRef | varchar | PK |  | NO | CTBB_Transaction Parent Reference |
| BBTRU_RowID | varchar |  |  | NO | - |
| BBTRU_UserGroup_DR | bigint |  | FK | NO | UserGroup DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*