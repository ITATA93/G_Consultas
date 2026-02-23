# SQLUser.PA_PersonConsultSet

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONSET_ParRef | bigint | PK |  | NO | PA_Consult Parent Reference |
| CONSET_Childsub | double |  |  | NO | Childsub |
| CONSET_ConsCategory_DR | bigint |  | FK | SI | Des Ref ConsCategory |
| CONSET_ConsSubCat_DR | varchar |  | FK | SI | Des Ref ConsSubCat |
| CONSET_Desc | varchar |  |  | SI | Description |
| CONSET_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*