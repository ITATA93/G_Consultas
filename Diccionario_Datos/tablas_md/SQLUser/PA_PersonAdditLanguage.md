# SQLUser.PA_PersonAdditLanguage

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADDITLANG_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| ADDITLANG_Childsub | double |  |  | NO | Childsub |
| ADDITLANG_DateEntered | date |  |  | SI | Date Entered |
| ADDITLANG_Language_DR | bigint |  | FK | SI | Des Ref to CTLAN |
| ADDITLANG_Rank | integer |  |  | SI | Rank |
| ADDITLANG_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*